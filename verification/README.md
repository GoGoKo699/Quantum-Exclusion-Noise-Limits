# Reproduce the finite checks

The universal threshold and asymptotic laws are established by the [analytical proofs](../science/README.md). This suite checks their algebraic representation, physical local measurement, and small unrestricted decision problems by separate constructions.

## Run

The reference run used Python 3.13.5 and the versions pinned in [requirements.txt](requirements.txt). From the repository root:

```sh
python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python verification/verify.py --output build/check.json
```

The output path must not exist. A failed assertion, singular construction, nonconverged optimization, or unacceptable feasibility/gap residual terminates with an error. The runner never overwrites an earlier result.

Expected terminal output:

```text
PASS: 7 algebra witnesses, 10 full-space adversarial checks, 16 numerical SDP brackets.
```

The committed [reference_results.json](reference_results.json) is the actual saved output, including package versions, every tested parameter, and feasibility diagnostics. Floating-point values and iteration counts can vary across platforms; exact byte equality is not required. Passing is determined by the explicit tolerances in the runner, not by a printed count alone.

## What each group checks

**Coefficient functional.** For a strict asymmetric triple with exact rational complex phases, SymPy constructs the coherent-symbol coefficient functional for $`n=1,\ldots,7`$. It verifies its trace against the exact positive coefficient of $`h^n`$. NumPy then independently builds the physical qubit rotations and symmetric Dicke basis to check annihilation of the high-error block, Hermiticity, and the claimed exponential norm bound.

**Full-space local protocol.** For trine and asymmetric triples, $`n=1,\ldots,5`$ and $`t=\lfloor(n-1)/3\rfloor`$, the code enumerates all outcome records, forms the actual $`2^n`$-dimensional POVM, and checks completeness and zero leakage on the entire allowed error subspace. This includes coherent superpositions, not just diagonal mixtures. These passing cases test sufficiency. The impossibility below threshold rests on the analytic coefficient argument, not on a failed solver search.

**Unrestricted noisy optimization.** For both triples, $`n=1,\ldots,4`$ and $`\delta=0.1,0.01`$, the code solves the finite exclusion SDP by a dual log-determinant path. It constructs a normalized positive primal POVM from the inverse dual slacks, then checks positivity, completeness, and the primal/dual gap. The trine uses equal priors; the asymmetric case uses priors $`(0.2,0.3,0.5)`$. All hypotheses are real after a common rotation, so taking the real part of a Hermitian POVM preserves positivity and risk: real symmetric optimization loses no strategies in these tests.

The final gap must be less than $`2\times10^{-7}`$, completeness residual below $`10^{-7}`$, primal eigenvalues above $`-10^{-9}`$, and dual slack eigenvalues above $`-10^{-12}`$. These are checked floating-point numerical brackets, **not interval-arithmetic certificates**. The trine one-copy exact value and an independently summed local counting risk provide additional controls.

## Limits

No finite run proves an all-$`n`$ theorem, an order of limits, literature priority, or hardware robustness. The geometric constant in the converse is deliberately conservative; the suite does not optimize it. No fixed-noise quantum exponent is extrapolated from these data. Source and numerical checks do not establish that every equation renders correctly on GitHub.

## Learning, navigation, and actual-host review

Run `python verification/check_repository.py` to check the thirty milestone records, backward-only dependency order, source links and text integrity. This verifies structure, not teaching effectiveness. The [hosted verification guide](references/hosted-rendering.md) documents commit-pinned GitHub captures at narrow and wide widths. The read-only CI workflow runs the scientific and repository checks and captures actual hosted MathML and screenshots. A source-only pass cannot replace that hosted comparison or visual inspection; each report identifies its checked revision.
