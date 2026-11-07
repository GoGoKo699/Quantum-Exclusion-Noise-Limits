# Quantum Exclusion Noise Limits

**How many imperfect preparations are needed to rule out a quantum state with certainty, and how does weak noise change the error rate?**

A source chooses one of three known pure qubit states and repeats that preparation. The receiver must name a state that was **not** chosen. For three distinct states whose Bloch triangle strictly contains the origin, separate measurements and a count decoder attain a sharp corruption threshold that no collective measurement can improve. Perfect exclusion of up to $`t`$ corruptions is possible if and only if

```math
\boxed{n\geq3t+1.}
```

The converse covers every joint POVM. It already holds against unknown-location product replacements; the attaining protocol also tolerates arbitrary states in the coherent span of the corresponding error patterns.

## Independent preparation noise

Let each received copy have eigenvalues $`1-\delta`$ and $`\delta`$, aligned with the nominal state and its orthogonal complement. For the optimum average exclusion error $`P_n^*(\delta)`$, put $`k_n=\lceil n/3\rceil`$. The [uniform finite-copy theorem](science/noise.md#uniform-error-bounds) gives

```math
\frac{\pi_{\min}\,\delta^{k_n}(1-\delta)^{n-k_n}}
 {12(n+1)B^n}
\leq P_n^*(\delta)\leq\min\{\pi_{\min},2^n\delta^{k_n}\},
```

where $`B`$ is an explicit constant depending only on the fixed triple, and the priors $`\pi_i`$ are fixed and positive. Thus the exact fixed-copy small-noise power is $`\lceil n/3\rceil`$. More importantly, the constants are controlled uniformly in $`n`$, so both lower and upper asymptotic error exponents have the same leading behavior:

```math
\underline E(\delta)=\tfrac13\log(1/\delta)+O(1),\qquad
\overline E(\delta)=\tfrac13\log(1/\delta)+O(1).
```

The limit at a fixed nonzero $`\delta`$ is not established. This is a sharp low-noise coefficient, not an exact fixed-noise exponent formula.

## Read the science

| Question | Authoritative account |
|---|---|
| What is supplied, charged, and optimized? | [Model and result map](science/model.md) |
| Why can no joint measurement beat the corruption threshold? | [Adversarial threshold](science/adversarial.md) |
| How does exact annihilation become a uniform noisy converse? | [Coefficient bound and noise law](science/noise.md) |
| What changes at an orthogonal-pair boundary? | [Interpretation and boundary controls](science/interpretation.md) |
| What is inherited, and what does this add? | [Related work](references/RELATED_WORK.md) |
| What has been checked computationally? | [Verification guide](verification/README.md) |

[The continuous science route](science/README.md) connects these proofs. [The compact reading map](llms.txt) routes theorem, conceptual, and reproduction questions.

## Learn the mechanism

The [learning introduction](learning/README.md) starts with a complete four-copy trine experiment. The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the author's standard-layout manuscript. The [source-to-project bridge](learning/WATROUS_BRIDGE.md) gives selected passages, translates notation, and supplies the polynomial and asymptotic steps locally.

Follow the [30-milestone map](learning/MILESTONES.md): 12 background/preliminaries milestones join the model's ingredients, and 18 narrative/innovation milestones develop the two theorems and their meaning. The specialist proof route remains directly accessible above.

## Reproduce the finite checks

```bash
python -m pip install -r verification/requirements.txt
python verification/check_repository.py
OPENBLAS_NUM_THREADS=1 python verification/verify.py --output /tmp/exclusion-check.json
```

The suite constructs exact coefficient witnesses, checks their action using independently built quantum matrices, verifies the local decoder on full error subspaces, and computes small-copy numerical primal/dual SDP brackets. These finite checks support the formulas; the universal threshold and asymptotic coefficient follow from the proofs.

## Scope and contact

The preparations are raw repetitions, not encoded codewords. Downstream measurements are ideal. The ensemble is known and fixed; no error locations, environmental records, or postselection are supplied. The local construction needs no coherent memory across copies. Geometry-dependent constants are not uniform as the triangle approaches degeneracy. Neither exact finite-noise optimality of the local decoder nor a general error-correction capacity is claimed.

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
