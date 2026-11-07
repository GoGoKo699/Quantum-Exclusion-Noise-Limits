# From Watrous to the exclusion theorems

**Anchor:** John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018). Source navigation below refers to the [author's standard-layout manuscript](https://jhwatrous.github.io/TQI.pdf), whose preface is dated January 2018, not the compact layout. The [author's book page](https://jhwatrous.github.io/books-and-courses.html) also provides individual chapters and errata. Page numbers below are the book's printed numbers; the linked full-PDF page is eight higher. The manuscript is linked, not redistributed.

This bridge supports the [30 milestones](MILESTONES.md). The book supplies mathematical foundations. The exclusion threshold, polynomial obstruction, and uniform noise conversion are developed locally and attributed separately from the [primary research literature](../references/RELATED_WORK.md).

## Selected reading, not an entire textbook

| Foundation needed here | Watrous passage | Project connection |
|---|---|---|
| Positive matrices and subspaces | §1.1.2, pp. 8–23 | A zero probability forces an effect to annihilate a vector. |
| Singular values and trace norm | §1.1.3, pp. 24–34, especially pp. 32–33 | A coefficient bound is converted into a quantitative leakage estimate. |
| Probability and convex optimization | §§1.2.2–1.2.3, pp. 47–56 | Outcome counts and the unrestricted exclusion optimization. |
| States of multiple registers | §§2.1.2–2.1.3, pp. 61–71 | Repeated preparations, mixed inputs, and inaccessible references. |
| General measurements | §§2.3.1–2.3.2, pp. 100–112 | The three-outcome qubit measurement and all allowed joint POVMs. |
| Decision problems for states | §§3.1.1–3.1.2, pp. 125–138 | Contrast the identification objective with exclusion. |
| Permutation symmetry | §7.1.1, pp. 391–399 | Compress to the symmetric sector and use its Dicke basis. |

The large-deviation calculation and elementary polynomial algebra needed below are supplied here and in the scientific proofs. Reading an additional algebra or statistics text is not a prerequisite.

## Notation and the decision rule

Watrous uses column vectors such as $`u`$, the adjoint $`u^*`$, positive operators, and measurements written as maps from outcomes to effects. Here $`|\psi\rangle`$ is a column vector, $`\langle\psi|`$ its adjoint, and $`\psi=|\psi\rangle\langle\psi|`$ the pure-state density matrix. Our $`M_i`$ is the effect for outcome $`i`$. The probability of that outcome on state $`\rho`$ is $`\mathrm{Tr}(M_i\rho)`$. The symbol $`\pi_i`$ denotes a prior probability; $`\Pi_n`$ denotes a projector, not a prior.

For identification, outcome $`i`$ is correct on hypothesis $`i`$. For exclusion it is wrong. Accordingly our risk is minimized:

```math
P_n(M)=\sum_{i=0}^2\pi_i\mathrm{Tr}
 \bigl[M_i\rho_i^{\otimes n}\bigr].
```

The effects obey positivity and sum to the identity. There is no inconclusive outcome. For full-rank noisy inputs, the associated dual problem maximizes $`\mathrm{Tr}Y`$ subject to $`Y\preceq\pi_i\rho_i^{\otimes n}`$ for each label. Weak duality follows by multiplying each inequality by $`M_i`$, taking traces and summing. This explains the numerical lower/upper risk brackets in [verification](../verification/README.md) without confusing a numerical optimizer with a universal proof.

All project logarithms are natural. A rate expressed in bits would be divided by $`\log2`$; no physical conclusion changes under a consistent base conversion.

## Why one copy can exclude a nonorthogonal state

A qubit density matrix has Bloch representation $`(I+\mathbf r\cdot\boldsymbol\sigma)/2`$, where a pure state's Bloch vector has length one. Its orthogonal complement has vector $`-\mathbf r`$. If a strict triangle surrounds the origin, there are positive weights with $`\sum_i w_i=1`$ and $`\sum_iw_i\mathbf r_i=0`$. Therefore

```math
F_i=2w_i|\phi_i\rangle\langle\phi_i|,
\qquad \sum_iF_i=I.
```

The probability of reporting $`i`$ on $`\psi_i`$ is zero. This is an inherited one-copy construction, not the new threshold theorem. For the trine, $`w_i=1/3`$ and the [opening experiment](README.md#one-complete-experiment) gives the complete outcome probabilities.

The strictness condition refers to the triangle's two-dimensional relative interior. A triangle has no three-dimensional interior. A common rotation places its great circle on the equator without changing any achievable risk.

## From individual records to coherent errors

A positive effect $`M`$ satisfies

```math
\langle v|M|v\rangle=\|\sqrt M\,v\|_2^2.
```

A zero expectation therefore implies $`\sqrt M\,v=0`$ and hence $`Mv=0`$. This turns a probabilistic statement into a linear one.

An allowed product error pattern has at most $`t`$ factors orthogonal to the nominal state. A record containing more than $`t`$ copies of the true label must assign that label to at least one honest site, so the square root of its record effect annihilates that product pattern. It annihilates every vector spanning the allowed error space, and therefore every superposition of those vectors. This is why the same decoder tolerates coherent error locations rather than only classical mixtures. Merely averaging zero probabilities without this positive-operator argument would leave that step unexplained.

## Compressing without restricting the receiver

Watrous's symmetric subspace contains vectors unchanged by permutations. For $`n`$ qubits it has an orthonormal basis $`|D_r\rangle`$, $`r=0,\ldots,n`$, where $`|D_r\rangle`$ is the normalized sum of bit strings with $`r`$ ones. In the basis adapted to $`(\psi_i,\phi_i)`$, $`r`$ counts orthogonal error factors.

Given any joint measurement, form $`A_i=\Pi_nM_i\Pi_n`$ on this subspace. These compressed effects are still positive and complete there. Perfect exclusion would force $`A_i`$ to vanish on error counts through $`t`$. It can only act on the higher-count span. We have extracted a necessary consequence of an arbitrary measurement; we have not assumed that the original input, errors, or receiver are symmetric.

## Turning support into polynomial factors

A degree-$`n`$ polynomial is a finite sum of monomials whose exponents total $`n`$. Map a symmetric vector with Dicke coefficients $`v_r`$ to

```math
p_v(x_0,x_1)=\sum_{r=0}^n v_r\sqrt{\binom nr}
 x_0^{n-r}x_1^r.
```

Tensor products of single-qubit vectors become products of linear factors after symmetrization. Thus a vector with at least $`K=t+1`$ error factors has the corresponding error linear form to power $`K`$ as a factor. An operator supported on that span factors in both its vector and conjugate-vector coordinates. The two sets of formal variables are independent; they are a way to encode a matrix, not extra physical systems.

The [coherent-symbol proof](../science/adversarial.md#a-polynomial-representation) names the resulting paired factor $`q_i`$. A perfect measurement would require the identity symbol $`h^n`$ to be a sum of three polynomials, respectively divisible by $`q_0^K`$, $`q_1^K`$, and $`q_2^K`$.

## The algebraic step that the book does not supply

Products $`x_ay_b`$ have the relation $`ad=bc`$ when $`a=x_0y_0`$, $`d=x_1y_1`$, $`b=x_1y_0`$, and $`c=x_0y_1`$. This relation means that one must not treat all four products as independent coordinates.

Set $`h=a+d`$ and $`s=a-d`$. Then $`s^2=h^2-4bc`$. Repeatedly replacing every $`s^2`$ reduces any expression uniquely to $`u+s v`$, with $`u,v`$ polynomials in $`h,b,c`$. Uniqueness follows from polynomial division by a monic quadratic in $`s`$. Taking the $`u`$ component commutes with multiplication by any polynomial in $`h,b,c`$.

For distinct equatorial states, the three $`q_i`$ are invertible linear coordinates for these three variables. This justifies doing coefficient comparisons in independent $`q`$ variables. The complete argument, including why the coordinate matrix is invertible, is in [the converse](../science/adversarial.md#why-the-relation-cannot-hold-below-the-threshold).

A monomial ideal generated by $`q_0^K,q_1^K,q_2^K`$ consists of sums with at least one exponent at least $`K`$ in every monomial. The identity has $`h=\sum_i c_iq_i`$ with all $`c_i\gt0`$. When $`n\leq3t`$, it has a nonzero coefficient at a monomial whose three exponents are at most $`t`$. That monomial is forbidden in the ideal. Completeness fails.

For the concrete trine case $`n=3,t=1`$, the coefficient of $`q_0q_1q_2`$ in $`h^3`$ is $`6(2/3)^3=16/9`$. None of $`q_0^2g_0,q_1^2g_1,q_2^2g_2`$ can contribute to that coefficient. This is the missing global argument behind the three-copy ambiguity in the opening example.

## Making an exact obstruction quantitative

At positive noise, no relevant probability is exactly zero. The proof instead extracts a chosen coefficient by a linear functional $`\mathcal L_n`$. It is positive on the identity and zero on each sufficiently high-error block. The essential estimate bounds its magnitude on an arbitrary matrix by a fixed geometric constant to power $`n`$ times that matrix's trace norm.

This growth control is indispensable. A bound with an uncontrolled constant depending on $`n`$ could prove a nonzero error at each fixed copy number while saying nothing useful about the many-copy rate.

The trace-norm estimate

```math
\|A-QAQ\|_1
\leq2\sqrt{\mathrm{Tr}A\,\mathrm{Tr}(PA)},
\qquad P+Q=I,\quad A\succeq0
```

turns a nonzero coefficient into unavoidable low-error weight. It follows by writing $`A-QAQ=PA+QAP`$ and applying Schatten Cauchy–Schwarz to factors involving $`\sqrt A`$. The [noise proof](../science/noise.md#quantitative-leakage-for-every-povm) gives the constants and connects this weight to the physical eigenvalues of the noisy preparations.

## Reading the noise sandwich in the right order

Let $`k_n=\lceil n/3\rceil`$. The theorem gives constants depending only on the fixed ensemble and fixed positive priors such that

```math
\frac{\pi_{\min}\delta^{k_n}(1-\delta)^{n-k_n}}
 {12(n+1)B^n}
\leq P_n^*(\delta)\leq2^n\delta^{k_n}.
```

First fix $`n`$ and send $`\delta`$ to zero. Both sides have the same power $`k_n`$; their constant factors can differ. Next, for the separate many-copy statement, fix $`\delta`$, take minus the logarithm divided by $`n`$, and use $`k_n/n\to1/3`$. The factor $`B^n`$ contributes only $`\log B`$, and the polynomial factor contributes a term tending to zero. Only after this step is $`\delta`$ sent to zero. This controls both liminf and limsup; it does not prove that they coincide at fixed noise.

The local noisy protocol has a binomial true-label count with success probability $`c_i\delta`$. For $`q\lt1/3`$, the exponential Markov bound applied to a binomial variable and optimized over its positive parameter gives

```math
\Pr\{\mathrm{Bin}(n,q)\geq n/3\}
\leq\exp[-nD_{\mathrm{bin}}(1/3\Vert q)].
```

Here $`D_{\mathrm{bin}}(p\Vert q)=p\log(p/q)+(1-p)\log[(1-p)/(1-q)]`$. This explains the local lower bound on the exponent. The [trine calculation](../science/noise.md#trine-example) identifies the exact classical exponent for that measurement, not the unrestricted quantum exponent.

## Return to the physical claim

The local construction is enough to reach the sharp threshold and leading low-noise coefficient. The converse explains why joint measurements cannot improve those two quantities under the stated preparation model. Finite-copy improvements remain possible, an orthogonal-pair boundary has a different law, and neither coding capacity nor a classical-versus-quantum advantage has been proved. Finish with [M29–M30](MILESTONES.md#m29) and the [scope discussion](../science/interpretation.md).
