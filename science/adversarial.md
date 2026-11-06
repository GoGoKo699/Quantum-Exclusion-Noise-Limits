# The exact corruption threshold

We prove Theorem A from the [model](model.md). The construction is local. The converse compresses an arbitrary joint POVM to the symmetric sector and uses completeness, rather than imposing a local-measurement restriction.

## Local construction

Measure every received qubit with $`F_i=c_i|\phi_i\rangle\langle\phi_i|`$. Let $`N_j`$ be the count of outcome $`j`$ and output a label of maximum count, breaking ties by a fixed rule.

For a true label $`i`$ and a product error pattern of weight at most $`t`$, an outcome record with $`N_i>t`$ has zero probability: at least one of the sites producing outcome $`i`$ must be honest, and $`F_i|\psi_i\rangle=0`$. More strongly, the positive square root of this record's tensor-product effect annihilates every generating vector of $`V_{i,t}`$. By linearity it annihilates the full error subspace. The conclusion therefore also holds for coherent and correlated adversarial inputs.

If $`n>3t`$, a maximum count exceeds $`t`$. Its label cannot be $`i`$. This proves sufficiency, including the strongest adversary in the model. No independence assumption is used here.

## Symmetric compression of any putative solution

Let $`\Pi_n`$ project onto $`\mathrm{Sym}^n(\mathbb C^2)`$, of dimension $`n+1`$, and put $`A_i=\Pi_nM_i\Pi_n`$ on that subspace. Then $`A_i\succeq0`$ and $`\sum_iA_i=I_{\mathrm{sym}}`$.

A positive operator with zero expectation on a vector annihilates that vector. If robust exclusion is perfect even for product replacements, $`M_i`$ annihilates all product patterns with at most $`t`$ factors $`\phi_i`$. Consequently $`A_i`$ annihilates the normalized symmetric Dicke vectors with error counts $`0,\ldots,t`$. Its support is contained in the remaining Dicke span with at least $`K=t+1`$ error factors.

If $`K>n`$, this already forces every $`A_i=0`$, a contradiction. The polynomial argument below includes that case by a zero high-error span.

## A polynomial representation

Use independent formal variables $`x_0,x_1,y_0,y_1`$. In the standard normalized Dicke basis, represent any operator $`A`$ by its coherent symbol

```math
f_A(x,y)=\sum_{r,s=0}^n A_{rs}
 \sqrt{\binom nr\binom ns}
 x_0^{n-r}x_1^r y_0^{n-s}y_1^s.
```

This is a linear bijection between operators and polynomials of bidegree $`(n,n)`$. In particular, $`f_{I_{\mathrm{sym}}}=h^n`$, where $`h=x_0y_0+x_1y_1`$. For a rank-one projector onto $`\phi_i`$, its degree-one symbol is

```math
q_i=\frac{(x_0-z_ix_1)(y_0-\overline z_i y_1)}2.
```

Every vector in the high-error symmetric span has a polynomial factor $`(x_0-z_ix_1)^K`$. Expanding an operator supported on this span as outer products shows that its symbol is divisible by $`q_i^K`$. Thus a perfect measurement would imply

```math
h^n=\sum_{i=0}^2q_i^K g_i
```

with $`g_i`$ of bidegree $`(n-K,n-K)`$.

## Why the relation cannot hold below the threshold

Introduce degree-one generators

```math
a=x_0y_0,\quad d=x_1y_1,\quad b=x_1y_0,\quad c=x_0y_1,
\qquad ad=bc.
```

The equal-bidegree polynomial ring is $`R=\mathbb C[a,b,c,d]/(ad-bc)`$. This presentation follows by pairing each $`x`$ factor with a $`y`$ factor; its degree-$`n`$ dimension is $`(n+1)^2`$, matching the coherent-symbol space.

Set $`s=a-d`$ and $`h=a+d`$. Then

```math
R=\mathbb C[h,b,c,s]/(s^2-h^2+4bc)
  =A\oplus sA,\qquad A=\mathbb C[h,b,c].
```

The second equality is a free-module decomposition: the defining polynomial is monic of degree two in $`s`$. Every element has a unique form $`u+s v`$ with $`u,v\in A`$.

The three $`q_i=(h-z_ib-\overline z_i c)/2`$ form an invertible linear coordinate system for $`A`$. Indeed, three distinct points on the unit circle cannot lie on a single real line; equivalently the matrix with rows $`(1,-z_i,-\overline z_i)`$ is nonsingular. Hence $`A=\mathbb C[q_0,q_1,q_2]`$. POVM completeness gives

```math
h=\sum_i c_iq_i,\qquad c_i>0.
```

Project $`R=A\oplus sA`$ onto its $`A`$ component. This projection is $`A`$-linear. The alleged perfect-measurement identity would therefore require

```math
h^n\in(q_0^K,q_1^K,q_2^K)A.
```

When $`n\leq3(K-1)`$, choose nonnegative integers $`\alpha_i\leq K-1`$ with sum $`n`$. The coefficient of $`q_0^{\alpha_0}q_1^{\alpha_1}q_2^{\alpha_2}`$ in $`h^n`$ is

```math
\frac{n!}{\alpha_0!\alpha_1!\alpha_2!}\prod_i c_i^{\alpha_i}>0.
```

Every polynomial in the displayed monomial ideal has zero coefficient at this monomial. This contradiction excludes every joint POVM when $`n\leq3t`$. Together with the construction, it proves the exact threshold $`n\geq3t+1`$.

## Role of the assumptions

Positivity converts zero expectations into support annihilation. Symmetric compression is a necessary consequence of an unrestricted measurement, not a restriction imposed on the receiver. Strict geometry supplies positive coefficients, preventing cancellation. A common subspace intersection alone would not give this converse; the obstruction is to *completeness* of the three effects.

The same coefficient extraction, with a controlled operator norm, yields the [noisy converse](noise.md). [Boundary controls](interpretation.md#an-orthogonal-pair-boundary) show why strictness cannot be dropped.
