# Meaning, resources, and boundary controls

## What collective measurements cannot change

For the strict triples in the [model](model.md), collective measurements cannot improve the exact number of adversarial corruptions that can be tolerated, or the leading small-noise coefficient of the many-copy error exponent. These are separate statements. Collective measurements can still improve finite-copy errors, constants, or a fixed-noise exponent; the theorem does not assert their universal uselessness.

For example, the verified trine calculation with three copies and $`\delta=0.01`$ brackets the unrestricted optimum near $`3.3562\times10^{-4}`$. This is a finite numerical result, not an asymptotic extrapolation; its numerical feasibility residuals and primal/dual gap are recorded in [the reference results](../verification/reference_results.json).

The key converse mechanism is not a dimension count or a restriction to product measurements. A complete joint measurement would need three positive effects whose coherent symbols lie in different powers of linear-factor ideals. A positive coefficient in the identity symbol prevents that completeness relation. Quantifying the coefficient functional transfers this zero-error obstruction to a nonzero lower bound uniform in copy number.

## Implementation and charges

The attaining protocol applies a known three-outcome qubit POVM independently to each received system. A fixed Naimark implementation can embed it in a four-dimensional space, using one clean ancillary qubit per measurement, recycled after readout. Equivalently, a native three-outcome detector may implement the specified POVM. This is an implementation of the fixed two-dimensional measurement, not a free preparation oracle.

The protocol uses $`n`$ copies, $`n`$ local measurement applications, and three counters requiring $`O(\log(n+1))`$ classical bits. It needs no inter-copy coherent memory or inter-copy entangling gates. Source preparation, detector calibration, ancilla reset where used, and measurement accuracy are physical costs not quantified by this ideal measurement model. The theorem is a copy-and-noise statement, not a hardware runtime advantage.

## Comparison with the general divergence converse

For these states,

```math
\log\rho_i=aI+b\,\mathbf r_i\cdot\boldsymbol\sigma,\quad
a=\tfrac12\log[\delta(1-\delta)],\quad
b=\tfrac12\log[(1-\delta)/\delta].
```

The general log-Euclidean upper bound evaluates to

```math
C_{\mathrm{LE}}=-\log\min_{s_i\geq0,\,\sum_i s_i=1}
\operatorname{Tr}\exp\!\left(\sum_i s_i\log\rho_i\right)
=-\log\bigl[2\sqrt{\delta(1-\delta)}\bigr].
```

Indeed the trace before minimization is $`2\sqrt{\delta(1-\delta)}\cosh(b|\sum_i s_i\mathbf r_i|)`$, and the origin is in the convex hull. The resulting leading coefficient is $`1/2`$, not $`1/3`$. The unrestricted noisy converse therefore strictly improves this benchmark at sufficiently small noise for each fixed strict triple. [Related work](../references/RELATED_WORK.md) identifies the source theorem and its precise regularization equivalence; this comparison does not claim that every conceivable divergence bound has been exhausted.

## An orthogonal-pair boundary

Strictness is essential. Consider the boundary triple $`|0\rangle,|1\rangle,|\chi\rangle`$, where $`|\chi\rangle=u|0\rangle+v|1\rangle`$ and $`uv\ne0`$. In our operational model, which permits unused output labels, its corruption threshold is instead $`n\geq2t+1`$.

For sufficiency, measure in the computational basis, identify the majority of zeroes or ones, and output the *opposite* basis-state label. For a true basis-state label at most $`t`$ reports are incorrect. For the third preparation either basis-state label is safe. The same record-effect argument as before covers the coherent error subspace.

For necessity when $`n\leq2t`$, choose a computational string $`x`$ whose Hamming weight lies between $`n-t`$ and $`t`$. It belongs to both basis states' error subspaces. Perfect exclusion forces $`M_0|x\rangle=M_1|x\rangle=0`$, and completeness forces $`M_2|x\rangle=|x\rangle`$. But exclusion of the uncorrupted third preparation forces $`M_2|\chi\rangle^{\otimes n}=0`$, contradicting $`\langle x|\chi\rangle^{\otimes n}\ne0`$.

Under independent mixing, the same binary measurement attains exponent $`-\log[2\sqrt{\delta(1-\delta)}]`$. The log-Euclidean converse above matches it. This is a boundary control using the established binary testing rate, not a claim that the strict-triple law extends to the boundary. The coefficient changes to $`1/2`$, and geometry-dependent constants in the interior theorem need not remain bounded as that boundary is approached.

## Endpoints and limits

At $`\delta=0`$, one-copy exclusion is perfect. At $`\delta=1/2`$, all preparations equal $`I/2`$, and $`P_n^*=\pi_{\min}`$ for every $`n`$. The lower bound for positive noise is consistent with both endpoints but need not be sharp there.

The result does not cover arbitrary noncoplanar triples, higher-dimensional ensembles, arbitrary noise channels, or encoded source states. It does not establish the existence or value of a fixed-noise quantum exponent in the strict interior. Simultaneous limits in which the ensemble geometry changes with $`n`$ or $`\delta`$ need separate control of the constants.
