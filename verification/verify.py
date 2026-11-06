#!/usr/bin/env python3
"""Finite checks for Quantum Exclusion Noise Limits; no asymptotic claims are inferred.

Run: OPENBLAS_NUM_THREADS=1 python verification/verify.py --output /tmp/exclusion.json
Dependencies are pinned in requirements.txt. All assertions raise explicitly.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
import platform
from functools import lru_cache
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import solve
import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def kron_power(a: np.ndarray, n: int) -> np.ndarray:
    out = np.ones((1, 1), dtype=a.dtype)
    for _ in range(n):
        out = np.kron(out, a)
    return out


def dicke(n: int) -> np.ndarray:
    u = np.zeros((2**n, n+1))
    for j in range(2**n):
        k = j.bit_count()
        u[j, k] = 1 / math.sqrt(math.comb(n, k))
    return u


def ensemble(angles: list[float]) -> tuple[list[np.ndarray], np.ndarray, list[np.ndarray]]:
    # A common rotation puts the great circle in the real x-z plane.
    rays = [np.array([np.cos(t/2), np.sin(t/2)]) for t in angles]
    r = np.array([[1, np.sin(t), np.cos(t)] for t in angles]).T
    weights = np.linalg.solve(r, np.array([1., 0., 0.]))
    require(bool(np.min(weights) > 0), 'The test ensemble is not strict.')
    c = 2 * weights
    effects = [c[i]*(np.eye(2)-np.outer(v, v)) for i, v in enumerate(rays)]
    require(np.linalg.norm(sum(effects)-np.eye(2)) < 1e-12, 'One-copy completeness')
    return rays, c, effects


def local_measurement(effects: list[np.ndarray], n: int) -> list[np.ndarray]:
    out = [np.zeros((2**n, 2**n)) for _ in range(3)]
    for record in itertools.product(range(3), repeat=n):
        counts = [record.count(i) for i in range(3)]
        label = int(np.argmax(counts))  # deterministic smallest-index tie rule
        a = np.ones((1, 1))
        for j in record:
            a = np.kron(a, effects[j])
        out[label] += a
    return out


def local_risk(rays: list[np.ndarray], effects: list[np.ndarray], n: int,
               delta: float, priors: np.ndarray) -> float:
    transition = np.array([[np.trace(f@((1-2*delta)*np.outer(v,v)+delta*np.eye(2)))
                            for f in effects] for v in rays])
    value = 0.
    for n0 in range(n+1):
        for n1 in range(n-n0+1):
            counts = np.array([n0, n1, n-n0-n1])
            j = int(np.argmax(counts))
            multiplicity = math.comb(n,n0)*math.comb(n-n0,n1)
            value += priors[j]*multiplicity*float(np.prod(transition[j]**counts))
    return value


def symmetric_basis(d: int) -> np.ndarray:
    out = []
    for j in range(d):
        for k in range(j,d):
            a = np.zeros((d,d))
            a[j,k] = a[k,j] = 1. if j == k else 1/math.sqrt(2)
            out.append(a)
    return np.array(out)


def numerical_sdp(costs: list[np.ndarray], tolerance: float = 1e-8) -> dict:
    """A dual log-det path, returning checked numerical primal/dual brackets.

    These are floating-point diagnostics, not interval-arithmetic certificates.
    No proof depends on solver termination. Feasibility and the final gap decide
    whether the result is usable. Real POVMs suffice for these real hypotheses.
    """
    d = costs[0].shape[0]
    basis = symmetric_basis(d)
    y = -np.eye(d)
    iterations = 0

    def evaluate(z: np.ndarray, mu: float, derivatives: bool = True):
        slacks = [c-z for c in costs]
        try:
            for s in slacks:
                np.linalg.cholesky(s)
        except np.linalg.LinAlgError:
            return None
        value = -np.trace(z)-mu*sum(np.linalg.slogdet(s)[1] for s in slacks)
        if not derivatives:
            return value
        inverses = []
        for s in slacks:
            a = np.linalg.inv(s)
            inverses.append((a+a.T)/2)
        g = np.einsum('aij,ij->a', basis, -np.eye(d)+mu*sum(inverses))
        h = sum(mu*np.einsum('aij,bji->ab', basis@a, basis@a) for a in inverses)
        return value, g, h

    for mu in np.geomspace(1., tolerance/(3*d), 18):
        for _ in range(80):
            value, g, h = evaluate(y, float(mu))
            step = solve(h, -g, assume_a='pos')
            if -g@step < max(1e-20, 1e-9*mu):
                break
            direction = np.einsum('a,aij->ij', step, basis)
            length = 1.
            for _ in range(70):
                candidate = evaluate(y+length*direction, float(mu), False)
                if candidate is not None and candidate <= value+.01*length*(g@step):
                    break
                length *= .5
            else:
                raise RuntimeError('SDP line search failed')
            y += length*direction
            y = (y+y.T)/2
            iterations += 1

    a = []
    for c in costs:
        z = np.linalg.inv(c-y)
        a.append(mu*(z+z.T)/2)
    s = sum(a)
    eigenvalues, vectors = np.linalg.eigh(s)
    require(bool(np.min(eigenvalues) > 0), 'Primal normalization is singular')
    root = (vectors*(1/np.sqrt(eigenvalues)))@vectors.T
    povm = [(root@z@root) for z in a]
    povm = [(z+z.T)/2 for z in povm]
    upper = float(sum(np.trace(c@m) for c,m in zip(costs,povm)))
    margin = float(min(np.linalg.eigvalsh(c-y)[0] for c in costs))
    lower = float(np.trace(y)-d*max(0., 1e-13-margin))
    completeness = float(np.linalg.norm(sum(povm)-np.eye(d)))
    primal_min = float(min(np.linalg.eigvalsh(m)[0] for m in povm))
    gap = upper-lower
    require(completeness < 1e-7 and primal_min > -1e-9, 'Primal feasibility failed')
    require(margin > -1e-12 and -1e-10 < gap < 2e-7, 'Dual feasibility/gap failed')
    return {'lower': lower, 'upper': upper, 'gap': gap,
            'completeness_residual': completeness, 'min_primal_eigenvalue': primal_min,
            'min_dual_slack_eigenvalue': margin, 'newton_steps': iterations}


def algebra_checks() -> list[dict]:
    """Build the coefficient functional exactly, test its matrix action separately."""
    q = sp.symbols('q0:3')
    phases = [sp.Integer(1), (-3+4*sp.I)/5, (-5-12*sp.I)/13]
    t = sp.Matrix([[sp.Rational(1,2), -z/2, -sp.conjugate(z)/2] for z in phases])
    inverse = t.inv()
    h,b,c = [sp.Poly(sum(row[j]*q[j] for j in range(3)),*q) for row in inverse.tolist()]
    discriminant = h*h-4*b*c
    cmin = min(float(h.coeff_monomial(qi)) for qi in q)
    ell = max(1., *(sum(abs(complex(z)) for z in p.coeffs()) for p in [h,b,c]))
    kgeom = (1+math.sqrt(5))*ell
    rows = []
    for n in range(1,8):
        alpha = tuple(n//3+int(i<n%3) for i in range(3))
        powers = [[p**r for r in range(n+1)] for p in [h,discriminant,b,c]]
        hp,dp,bp,cp = powers
        w = sp.zeros(n+1,n+1)
        for j in range(n+1):
            for k in range(n+1):
                r,s = n-max(j,k), min(j,k)
                u,v = max(j-k,0), max(k-j,0)
                poly = sp.Poly(0,*q)
                for l in range(r+1):
                    for m in range(s+1):
                        if (l+m)%2 == 0:
                            factor = sp.Rational(math.comb(r,l)*math.comb(s,m)*(-1)**m,2**(r+s))
                            poly += factor*hp[r+s-l-m]*dp[(l+m)//2]
                poly *= bp[u]*cp[v]
                w[k,j] = sp.sqrt(math.comb(n,j)*math.comb(n,k))*poly.coeff_monomial(alpha)
        target = (h**n).coeff_monomial(alpha)
        require(sp.simplify(sp.trace(w)-target) == 0, 'Exact identity coefficient')
        require(target > 0, 'Strict positive witness coefficient')
        matrix = np.array(w.evalf(),complex)
        norm = float(np.linalg.norm(matrix,2))
        require(np.linalg.norm(matrix-matrix.conj().T) < 1e-10, 'Hermitian witness')
        require(norm <= kgeom**n*(1+1e-12), 'Coefficient norm bound')
        u = dicke(n)
        threshold = (n+2)//3
        residual = 0.
        for z in phases:
            z = complex(z)
            rotation = np.array([[1,1],[z,-z]])/math.sqrt(2)
            v = u.T@kron_power(rotation,n)@u
            high = v[:,threshold+1:]
            if high.shape[1]:
                residual = max(residual,float(np.linalg.norm(high.conj().T@matrix@high)/max(1,norm)))
        require(residual < 1e-10, 'Functional fails to annihilate the high-error block')
        rows.append({'n':n,'balanced_exponents':alpha,'identity_coefficient':str(target),
                     'witness_operator_norm':norm,'relative_high_block_residual':residual,
                     'K_geometry':kgeom,'B_geometry':(kgeom/cmin)**2})
    return rows


def run() -> dict:
    sets = {'trine':[0.,2*np.pi/3,4*np.pi/3],
            'asymmetric':[0.,float(np.angle(-3+4j)),float(np.angle(-5-12j))]}
    report = {'versions':{'python':platform.python_version(),'numpy':np.__version__,
                         'scipy':scipy.__version__,'sympy':sp.__version__},
              'algebra':algebra_checks(),'adversarial':[],'noisy_sdp':[],
              'scope':'Finite exact algebra and floating-point matrix checks only; universal claims are analytical.'}
    for name,angles in sets.items():
        rays,c,effects = ensemble(angles)
        for n in [1,2,3,4,5]:
            m = local_measurement(effects,n)
            t = (n-1)//3
            leakage = 0.
            u = dicke(n)
            for i,psi in enumerate(rays):
                phi = np.array([-psi[1],psi[0]])
                v = kron_power(np.stack([psi,phi],axis=1),n)
                indices = [j for j in range(2**n) if j.bit_count() <= t]
                low = v[:,indices]
                leakage = max(leakage,float(np.linalg.norm(low.T@m[i]@low)))
            complete = float(np.linalg.norm(sum(m)-np.eye(2**n)))
            require(leakage < 1e-10 and complete < 1e-10, 'Local adversarial protocol')
            report['adversarial'].append({'ensemble':name,'n':n,'t':t,
                'low_subspace_leakage':leakage,'completeness_residual':complete})
        priors = np.array([1/3]*3) if name=='trine' else np.array([.2,.3,.5])
        for n in [1,2,3,4]:
            for delta in [.1,.01]:
                costs = [priors[i]*kron_power((1-2*delta)*np.outer(v,v)+delta*np.eye(2),n)
                         for i,v in enumerate(rays)]
                bracket = numerical_sdp(costs)
                local = local_risk(rays,effects,n,delta,priors)
                require(bracket['lower'] <= local+1e-9, 'Local protocol below dual bound')
                require(local <= 2**n*delta**((n+2)//3)+1e-12, 'Elementary local upper bound')
                if n==1 and name=='trine':
                    require(bracket['lower']-1e-10 <= 2*delta/3 <= bracket['upper']+1e-10,
                            'Exact one-copy trine value')
                report['noisy_sdp'].append({'ensemble':name,'n':n,'delta':delta,
                                          'local_risk':local,**bracket})
    report['passed'] = True
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Use a new output path; existing evidence is not overwritten.')
    result = run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS: 7 algebra witnesses, 10 full-space adversarial checks, 16 numerical SDP brackets.')
