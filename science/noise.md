# From exact exclusion to a uniform noise law

A fixed-copy expansion cannot by itself control a many-copy error exponent. Here the coefficient obstruction from [the adversarial proof](adversarial.md) is made quantitative, with constants growing at most exponentially in the number of copies.

## Coefficient functional and its norm

Retain the ring $`R=A\oplus sA`$, the coordinates $`q_i`$, and $`h=\sum_i c_iq_i`$. Set $`k=\lceil n/3\rceil`$ and choose a balanced triple $`\alpha`$ with sum $`n`$ and $`\alpha_i\leq k`$. Define $`\mathcal L_n(A)`$ to be the $`q^\alpha`$ coefficient in the $`A`$-component of $`f_A`$. Then

```math
\mathcal L_n(I_{\mathrm{sym}})
=\frac{n!}{\alpha_0!\alpha_1!\alpha_2!}\prod_i c_i^{\alpha_i}
\geq c_{\min}^n,\qquad c_{\min}=\min_i c_i>0.
```

For a polynomial in the $`q`$ coordinates let $`\|\cdot\|_{\mathrm{coef},1}`$ denote the sum of absolute coefficients. Express the linear forms $`h,b,c`$ by inverting the three-by-three coordinate matrix in the adversarial proof, and define

```math
L=\max\{1,\|h\|_{\mathrm{coef},1},\|b\|_{\mathrm{coef},1},
                  \|c\|_{\mathrm{coef},1}\},\qquad
K=(1+\sqrt5)L,\qquad B=(K/c_{\min})^2.
```

These are finite constants for each fixed strict triple. We claim

```math
|\mathcal L_n(A)|\leq K^n\|A\|_1. \tag{N1}
```

To prove this, write a degree-$`n`$ monomial as $`a^r d^u b^v c^w`$. Substitute $`a=(h+s)/2`$, $`d=(h-s)/2`$ and reduce $`s^2=\Delta=h^2-4bc`$. Since $`\|\Delta\|_{\mathrm{coef},1}\leq5L^2`$, the coefficient one-norm of its $`A`$-component is at most $`\gamma^n`$, where $`\gamma=(1+\sqrt5)L/2`$. This follows by summing the even-$`s`$ terms in the binomial expansion and bounding their absolute coefficients; the omitted odd terms can only increase that upper bound.

For a normalized outer product $`|u\rangle\langle v|`$, the Dicke normalization factors obey

```math
\sum_{j=0}^n|u_j|\sqrt{\binom nj}\leq2^{n/2}\|u\|_2,
\qquad
\sum_{j=0}^n|v_j|\sqrt{\binom nj}\leq2^{n/2}\|v\|_2.
```

Thus the coefficient bound is $`(2\gamma)^n=K^n`$. A singular-value decomposition proves (N1) for arbitrary operators. There is no uncharged factor growing faster than exponentially in $`n`$.

## Quantitative leakage for every POVM

Compress an arbitrary POVM to $`A_i=\Pi_nM_i\Pi_n`$. In the symmetric Dicke basis relative to $`(\psi_i,\phi_i)`$, let $`P_i`$ project onto counts $`0,\ldots,k`$, and $`Q_i=I-P_i`$. Put $`\varepsilon_i=\operatorname{Tr}(P_iA_i)`$.

The symbol of $`Q_iA_iQ_i`$ is divisible by $`q_i^{k+1}`$, so
$`\mathcal L_n(Q_iA_iQ_i)=0`$. For any positive operator $`A`$ and projector $`Q=I-P`$,

```math
\|A-QAQ\|_1\leq2\sqrt{\operatorname{Tr}(A)\operatorname{Tr}(PA)}.
```

For completeness, decompose $`A-QAQ=PA+QAP`$, insert $`\sqrt A\sqrt A`$, and use the Schatten Cauchy--Schwarz inequality on both terms. Since $`0\preceq A_i\preceq I_{\mathrm{sym}}`$, its trace is at most $`n+1`$. Applying (N1), then ordinary Cauchy--Schwarz over the three labels, gives

```math
c_{\min}^n
\leq2K^n\sqrt{n+1}\sum_i\sqrt{\varepsilon_i}
\leq2K^n\sqrt{3(n+1)\sum_i\varepsilon_i}.
```

Consequently every POVM has

```math
\sum_i\varepsilon_i\geq\frac1{12(n+1)B^n}. \tag{N2}
```

This step permits measurements that depend on $`\delta`$ and includes all nonsymmetric sectors through the original unrestricted POVM. Compression only extracts a necessary positive contribution to its risk.

## Uniform error bounds

In the $`i`$-adapted Dicke basis, $`\rho_i(\delta)^{\otimes n}`$ has eigenvalue $`\delta^r(1-\delta)^{n-r}`$ on error count $`r`$. For $`r\leq k`$ and $`\delta<1/2`$, these eigenvalues are at least $`\delta^k(1-\delta)^{n-k}`$. Therefore (N2) proves

```math
P_n^*(\delta)\geq
\frac{\pi_{\min}\delta^k(1-\delta)^{n-k}}{12(n+1)B^n}. \tag{N3}
```

The explicit $`\pi_{\min}`$ is necessary when the objective is prior-weighted average error. The inequality holds for every $`n\geq1`$ and $`0<\delta<1/2`$.

For the attaining local construction, each measurement reports the true label $`i`$ with probability $`c_i\delta`$. Independent preparation noise makes that label's count binomial. Outputting the maximum-count label can be wrong only when $`N_i\geq k`$. Hence

```math
P_n^*(\delta)\leq P_n^{\mathrm{count}}(\delta)
\leq\sum_i\pi_i\Pr\{\mathrm{Bin}(n,c_i\delta)\geq k\}
\leq2^n\delta^k. \tag{N4}
```

Always outputting a least-probable label also gives $`P_n^*\leq\pi_{\min}`$. Equations (N3)--(N4) establish the exact fixed-$`n`$ small-noise power $`k`$.

## The asymptotic order of limits

Put $`c_{\max}=\max_i c_i`$. When $`c_{\max}\delta<1/3`$, the elementary binomial Chernoff bound improves (N4) to

```math
\underline E(\delta)\geq D_{\mathrm{bin}}(1/3\Vert c_{\max}\delta),
```

where $`D_{\mathrm{bin}}(p\Vert q)=p\log(p/q)+(1-p)\log((1-p)/(1-q))`$. Applying (N3) and using $`k/n\to1/3`$ yields the full comparison

```math
D_{\mathrm{bin}}(1/3\Vert c_{\max}\delta)
\leq\underline E(\delta)\leq\overline E(\delta)
\leq\log B+\frac13\log\frac1\delta+\frac23\log\frac1{1-\delta}. \tag{N5}
```

Both ends have leading term $`\frac13\log(1/\delta)`$ as $`\delta\downarrow0`$. This proves Theorem B without assuming a fixed-noise limit. The additive constants can depend on the fixed geometry, not on $`n`$ or $`\delta`$ in a sufficiently small-noise interval. Priors remain fixed and positive.

## Trine example

For $`z_j=e^{2\pi\mathrm{i}j/3}`$, $`c_i=2/3`$. With equal priors the local measurement has conditional probabilities $`a=2\delta/3`$ for the true label and $`b=(1-a)/2`$ for either other label. Its optimal classical postprocessing is exactly the maximum-count rule, because $`a<b`$.

Its classical exclusion exponent is

```math
E_{\mathrm{count}}(\delta)=-\log\!\bigl[3(a b^2)^{1/3}\bigr]
=D_{\mathrm{bin}}(1/3\Vert a).
```

This follows either from the established classical exclusion theorem cited in [Related work](../references/RELATED_WORK.md), or directly by a type calculation: an error requires the true-label count to be maximal; the minimizing type has all three frequencies $`1/3`$. Balanced integer types approach this boundary and have only polynomial prefactors. Thus

```math
E_{\mathrm{count}}(\delta)=\frac13\log(1/\delta)-\frac13\log(9/2)+o(1).
```

The local exponent formula is not asserted to equal the unrestricted quantum exponent at fixed noise. Finite-copy SDP calculations can give strictly smaller quantum error than this local protocol while retaining the same sharp small-noise power.
