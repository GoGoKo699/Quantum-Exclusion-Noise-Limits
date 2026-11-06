# Repeated preparations and excluded labels

State exclusion asks for a label that is wrong, rather than the correct preparation label. This distinction makes perfect one-copy exclusion possible for some nonorthogonal triples. Our question is how robust that capability is when the source supplies repeated, imperfect preparations.

## Ensemble and decision

Let $`\psi_i=|\psi_i\rangle\langle\psi_i|`$, $`i=0,1,2`$, be three distinct pure qubit states. Their Bloch vectors lie on a great circle and their nondegenerate triangle contains the origin in its **strict relative interior**. Equivalently, unique weights satisfy

```math
w_i>0,\qquad \sum_iw_i=1,\qquad \sum_iw_i\mathbf r_i=0.
```

The triangle has two-dimensional relative interior, not interior in the full three-dimensional Bloch ball. A common known unitary places it on the equator, where

```math
|\psi_i\rangle=(|0\rangle+z_i|1\rangle)/\sqrt2,\quad
|\phi_i\rangle=(|0\rangle-z_i|1\rangle)/\sqrt2,\quad |z_i|=1.
```

Write $`c_i=2w_i`$. Strictness and distinctness imply $`0<c_i<1`$, and the established one-copy exclusion POVM is

```math
F_i=c_i|\phi_i\rangle\langle\phi_i|,\qquad \sum_iF_i=I.
```

This construction and the Bloch-convexity criterion are prior ingredients, attributed in [Related work](../references/RELATED_WORK.md). The new work concerns robustness under repeated preparation and unrestricted measurements.

The source chooses one fixed label $`i`$. A receiver using $`n\geq1`$ copies performs any POVM $`(M_0,M_1,M_2)`$ on $`(\mathbb C^2)^{\otimes n}`$ and outputs its outcome. An error occurs exactly when that outcome is $`i`$. Zero effects are allowed; no inconclusive outcome is allowed. The strict-triple attaining protocol nevertheless uses all three output labels with positive probability on some ideal input.

## Unknown-location corruption

For each label, define the error subspace

```math
V_{i,t}=\operatorname{span}\!\left\{
\bigotimes_{a=1}^n|v_a\rangle:
 |v_a\rangle\in\{|\psi_i\rangle,|\phi_i\rangle\},\quad
 \#\{a:|v_a\rangle=|\phi_i\rangle\}\leq t\right\}.
```

Here $`0\leq t\leq n`$ is an integer. Our strongest allowed adversary supplies any density operator supported on $`V_{i,t}`$, with label-dependent choices. This includes coherent superpositions of error locations, correlations among corrupted systems, arbitrary replacement on an unknown subset of at most $`t`$ systems, and mixtures of such replacements. An inaccessible purifying reference does not change the reduced-state guarantee. It does not include arbitrary noise constrained only by its *mean* number of errors.

Perfect robust exclusion means $`\operatorname{Tr}(M_i\omega)=0`$ for every allowed $`\omega`$ and every label. The same sharp threshold holds for the weaker adversary restricted to product replacements: the lower bound already uses product error patterns, while the upper bound covers their entire coherent span.

**Theorem A.** Under this experiment, robust perfect exclusion is possible if and only if $`n\geq3t+1`$. See the [complete proof](adversarial.md).

## Independent mixing

For $`0<\delta<1/2`$, let

```math
\rho_i(\delta)=(1-\delta)\psi_i+\delta|\phi_i\rangle\langle\phi_i|.
```

The receiver obtains $`\rho_i(\delta)^{\otimes n}`$. Fix priors $`\pi_i>0`$ with sum one, independent of $`n`$ and $`\delta`$, and define

```math
P_n^*(\delta)=\min_{M_i\succeq0,\,\sum_iM_i=I}
 \sum_i\pi_i\operatorname{Tr}[M_i\rho_i(\delta)^{\otimes n}].
```

The minimization allows noise-dependent collective POVMs. Define the two rates separately:

```math
\underline E(\delta)=\liminf_{n\to\infty}-\frac1n\log P_n^*(\delta),\qquad
\overline E(\delta)=\limsup_{n\to\infty}-\frac1n\log P_n^*(\delta).
```

All logarithms are natural. Positive fixed priors change risks only by constant factors, so they do not change these asymptotic rates.

**Theorem B.** The explicit [finite-copy bounds](noise.md#uniform-error-bounds) imply, for each fixed strict triple,

```math
\lim_{\delta\downarrow0}\frac{\underline E(\delta)}{\log(1/\delta)}
=\lim_{\delta\downarrow0}\frac{\overline E(\delta)}{\log(1/\delta)}=\frac13.
```

They also prove $`P_n^*(\delta)=\Theta_{n,\psi,\pi}(\delta^{\lceil n/3\rceil})`$ at each fixed $`n`$. The theorem does not interchange these limits or assert their equality at fixed noise.

## Resource boundary

The source supplies raw identical preparations. All received copies count. There is no pre-noise encoding, state-preparation oracle, inverse preparation, environmental measurement, error-location flag, or postselection. Known operations and downstream measurements are ideal; arbitrary joint POVMs are allowed in the converse. The attaining protocol measures one qubit at a time and stores three integer counts. Its resources and limitations are discussed in [Interpretation](interpretation.md).
