# The 30-milestone understanding map

This map follows one logical route through the project. **M01–M12 are background/preliminaries; M13–M30 are narrative/innovation.** Twelve background milestones are needed because the converse connects quantum measurements, symmetric tensors, and polynomial coefficients. The remaining eighteen assemble the threshold, its uniform noise conversion, and their physical interpretation. Each phase ends by integrating its earlier components.

The sole educational anchor is **Watrous, *The Theory of Quantum Information* (2018), standard-layout author manuscript**. Section/page details and locally supplied prerequisites are in the [bridge](WATROUS_BRIDGE.md#selected-reading-not-an-entire-textbook). Primary research references remain attribution, not additional educational anchors. Follow increasing milestone number; the dependencies below identify the load-bearing earlier concepts.

## Background and preliminaries

<a id="m01"></a>
### M01 — Exclude a label rather than identify it

**Question:** What counts as an error in this experiment?

**Target:** Explain why reporting the actual preparation is wrong, why no inconclusive answer is allowed, and why this differs from identifying a state. **Dependencies:** None. **Connection and role:** The operational output fixes every later risk and decoder convention. **Sources:** Watrous §3.1 as a discrimination contrast; [model](../science/model.md#ensemble-and-decision); [bridge notation](WATROUS_BRIDGE.md#notation-and-the-decision-rule).

<a id="m02"></a>
### M02 — Pure states, mixing, and an orthogonal direction

**Question:** What does one noisy preparation represent?

**Target:** Distinguish a state vector from its density matrix and read eigenvalues $`1-\delta`$ and $`\delta`$ in the nominal/orthogonal basis. **Dependencies:** M01. **Connection and role:** A physical error probability becomes a spectral weight used in the noisy converse. **Sources:** Watrous §2.1.2; [independent mixing](../science/model.md#independent-mixing).

<a id="m03"></a>
### M03 — Outcomes as positive effects

**Question:** How can a qubit have a three-outcome measurement?

**Target:** Use positive effects summing to identity to obtain normalized probabilities; distinguish a general POVM from an orthogonal-basis measurement. **Dependencies:** M02. **Connection and role:** The local construction and unrestricted collective comparator share the same measurement framework. **Sources:** Watrous §§2.3.1–2.3.2; [one-copy bridge](WATROUS_BRIDGE.md#why-one-copy-can-exclude-a-nonorthogonal-state).

<a id="m04"></a>
### M04 — Zero probability forces annihilation

**Question:** Why is positivity stronger than a vanishing matrix entry?

**Target:** Derive $`Mv=0`$ from $`M\succeq0`$ and a zero expectation, using the positive square root. **Dependencies:** M03. **Connection and role:** Probabilistic zero-error conditions become linear support constraints. **Sources:** Watrous §1.1.2; [coherent-error bridge](WATROUS_BRIDGE.md#from-individual-records-to-coherent-errors).

<a id="m05"></a>
### M05 — Repetition of one fixed hypothesis

**Question:** What is independent, and what stays the same across copies?

**Target:** Explain conditional independence under independent mixing while retaining a single preparation label; distinguish repeated hypotheses from independently chosen labels and encoded codewords. **Dependencies:** M02–M03. **Connection and role:** This fixes the tensor-power experiment and prevents a coding-capacity interpretation. **Sources:** Watrous §§2.1.2–2.1.3; [resource boundary](../science/model.md#resource-boundary).

<a id="m06"></a>
### M06 — An error subspace is more than a mixture

**Question:** Which corrupted inputs must a robust measurement handle?

**Target:** Distinguish unknown-location product replacements, mixtures, and coherent superpositions within their span; identify what a weight cutoff excludes. **Dependencies:** M04–M05. **Connection and role:** Linearity carries the local guarantee to the strongest declared adversary. **Sources:** Watrous §1.1.1 and §2.1.3; [corruption model](../science/model.md#unknown-location-corruption).

<a id="m07"></a>
### M07 — Strict Bloch geometry and an inherited POVM

**Question:** Why does a triangle surrounding the origin matter?

**Target:** Translate positive convex weights into a complete exclusion POVM and interpret strict relative interior correctly. **Dependencies:** M02–M03. **Connection and role:** Geometry supplies the one-copy measurement and positive coefficients needed later. **Sources:** Watrous §§1.2.1, 2.3; [Bloch bridge](WATROUS_BRIDGE.md#why-one-copy-can-exclude-a-nonorthogonal-state); [prior criterion](../references/RELATED_WORK.md#one-copy-qubit-exclusion).

<a id="m08"></a>
### M08 — Norms measure the size of a correction

**Question:** What quantitative control survives when zero error becomes small error?

**Target:** Interpret trace norm, singular values and Schatten Cauchy–Schwarz without identifying them with a probability. **Dependencies:** M04. **Connection and role:** A matrix correction can be bounded by the square root of its unwanted support weight. **Sources:** Watrous §1.1.3; [quantitative bridge](WATROUS_BRIDGE.md#making-an-exact-obstruction-quantitative).

<a id="m09"></a>
### M09 — The unrestricted optimization and its dual

**Question:** What is optimized in a finite-copy numerical check?

**Target:** Form the exclusion risk over all POVMs, derive weak duality, and distinguish feasible bounds from solver status alone. **Dependencies:** M01–M03, M08. **Connection and role:** The numerical comparator must match the analytical receiver class. **Sources:** Watrous §§1.2.3, 3.1.2; [decision bridge](WATROUS_BRIDGE.md#notation-and-the-decision-rule); [verification](../verification/README.md).

<a id="m10"></a>
### M10 — Symmetric vectors and error-count bases

**Question:** What information is retained by symmetric compression?

**Target:** Construct the normalized Dicke basis, count its $`n+1`$ dimensions, and distinguish a permutation-invariant vector from a general invariant density operator. **Dependencies:** M05–M06. **Connection and role:** A small necessary sector can obstruct a measurement acting on the full tensor product. **Sources:** Watrous §7.1.1; [compression bridge](WATROUS_BRIDGE.md#compressing-without-restricting-the-receiver).

<a id="m11"></a>
### M11 — Monomials, factors, and matrix symbols

**Question:** How can polynomial coefficients encode a quantum operator?

**Target:** Read degrees and divisibility; map Dicke coefficients to a homogeneous polynomial and outer products to two variable sets. **Dependencies:** M10. **Connection and role:** Repeated orthogonal factors become a coefficient obstruction rather than a dimension heuristic. **Sources:** [local polynomial introduction](WATROUS_BRIDGE.md#turning-support-into-polynomial-factors); Watrous §§1.1.1–1.1.2 for vector/operator foundations only.

<a id="m12"></a>
### M12 — Assemble the experiment and its three limits

**Question:** Which resources, quantifiers, and limits belong to each claim?

**Target:** State the adversarial task, the fixed-copy small-noise task, and the many-copy rates with fixed geometry and positive priors. **Dependencies:** M01–M11. **Connection and role:** This background synthesis separates the exact threshold from two distinct limiting operations. **Sources:** [full model](../science/model.md); [order-of-limits bridge](WATROUS_BRIDGE.md#reading-the-noise-sandwich-in-the-right-order).

## Narrative and innovation

<a id="m13"></a>
### M13 — Build the local exclusion measurement

**Question:** How do the strict-triple weights determine the actual receiver?

**Target:** Verify completeness and the forbidden same-label probability; recover the trine's two equally likely safe labels. **Dependencies:** M07, M12. **Connection and role:** The known one-copy ingredient becomes an explicit component of the robustness construction. **Sources:** [model geometry](../science/model.md#ensemble-and-decision); [worked experiment](README.md#one-complete-experiment); Watrous §2.3.

<a id="m14"></a>
### M14 — Prove a record-wise corruption guarantee

**Question:** Why can the true label never be counted more than $`t`$ times?

**Target:** Prove annihilation for each offending record on every product error generator, then extend it to the whole coherent error span. **Dependencies:** M04, M06, M13. **Connection and role:** This establishes the guarantee without falsely assuming independent adversarial errors. **Sources:** [local construction](../science/adversarial.md#local-construction); [coherent-error bridge](WATROUS_BRIDGE.md#from-individual-records-to-coherent-errors).

<a id="m15"></a>
### M15 — Turn counts into the sufficient threshold

**Question:** Why does a maximum-count label give a safe output?

**Target:** Apply the three-counter pigeonhole argument at $`n\gt3t`$, including ties, and distinguish failure of this rule below threshold from impossibility for all measurements. **Dependencies:** M01, M14. **Connection and role:** The constructive half of the threshold is complete; the converse remains a different problem. **Sources:** [local proof](../science/adversarial.md#local-construction); [four-copy example](README.md#one-complete-experiment).

<a id="m16"></a>
### M16 — Extract a necessary sector from any POVM

**Question:** Why is symmetric compression legitimate for a global converse?

**Target:** Show positivity and completeness of the compressed effects and their annihilation of low-error Dicke vectors. **Dependencies:** M04, M06, M10, M12. **Connection and role:** Every possible receiver must satisfy this necessary algebraic condition. **Sources:** [compression proof](../science/adversarial.md#symmetric-compression-of-any-putative-solution); Watrous §7.1.1.

<a id="m17"></a>
### M17 — Translate high-error support into divisibility

**Question:** Which factor must every compressed effect contain?

**Target:** Derive the paired factor $`q_i^{t+1}`$ in the coherent symbol and identify $`h^n`$ as the identity symbol. **Dependencies:** M11, M16. **Connection and role:** Operator completeness becomes a polynomial membership question. **Sources:** [polynomial representation](../science/adversarial.md#a-polynomial-representation); [bridge](WATROUS_BRIDGE.md#turning-support-into-polynomial-factors).

<a id="m18"></a>
### M18 — Respect the relation among paired variables

**Question:** Why cannot the four paired coordinates be treated as independent?

**Target:** Derive $`ad=bc`$ from the two variable sets and understand the equal-bidegree polynomial ring. **Dependencies:** M11, M17. **Connection and role:** This prevents an invalid coefficient comparison in an oversized polynomial space. **Sources:** [ring argument](../science/adversarial.md#why-the-relation-cannot-hold-below-the-threshold); [local algebra bridge](WATROUS_BRIDGE.md#the-algebraic-step-that-the-book-does-not-supply).

<a id="m19"></a>
### M19 — Project to independent exclusion coordinates

**Question:** How are coefficient comparisons justified despite the relation?

**Target:** Use reduction by the monic quadratic in $`s`$, explain the unique two-component form, and verify the invertibility of the three $`q_i`$ coordinates. **Dependencies:** M07, M18. **Connection and role:** The projection preserves each required divisibility relation. **Sources:** [free-module proof](../science/adversarial.md#why-the-relation-cannot-hold-below-the-threshold); [algebra bridge](WATROUS_BRIDGE.md#the-algebraic-step-that-the-book-does-not-supply).

<a id="m20"></a>
### M20 — Find the coefficient that completeness cannot supply

**Question:** What contradicts perfect exclusion when $`n\leq3t`$?

**Target:** Choose exponents at most $`t`$ whose sum is $`n`$, show their identity coefficient is positive, and show it vanishes in the required ideal. **Dependencies:** M17, M19. **Connection and role:** This is the unrestricted impossibility argument, not a local-decoder lower bound. **Sources:** [converse coefficient](../science/adversarial.md#why-the-relation-cannot-hold-below-the-threshold); [three-copy trine coefficient](WATROUS_BRIDGE.md#the-algebraic-step-that-the-book-does-not-supply).

<a id="m21"></a>
### M21 — Combine both directions and test the boundary

**Question:** What exactly makes the threshold sharp?

**Target:** Combine M15 and M20, include $`t=0`$, and explain why an orthogonal-pair boundary instead permits the $`2t+1`$ law. **Dependencies:** M15, M20. **Connection and role:** The first global result is understood together with a load-bearing geometric limitation. **Sources:** [Theorem A](../science/model.md#unknown-location-corruption); [boundary proof](../science/interpretation.md#an-orthogonal-pair-boundary).

<a id="m22"></a>
### M22 — Identify what an exact obstruction does not yet prove

**Question:** Why is zero-error impossibility insufficient for a noisy exponent?

**Target:** Distinguish a nonzero risk for each fixed $`n`$ from a lower bound whose constants stay controlled as $`n`$ grows. **Dependencies:** M08, M12, M21. **Connection and role:** This motivates the uniform quantitative part rather than extrapolating a finite-size calculation. **Sources:** [noise introduction](../science/noise.md); [quantitative bridge](WATROUS_BRIDGE.md#making-an-exact-obstruction-quantitative).

<a id="m23"></a>
### M23 — Extract a balanced coefficient as a linear functional

**Question:** Which piece of the identity can detect unavoidable leakage?

**Target:** Define the balanced coefficient functional, compute its positive identity value, and explain why it annihilates blocks above $`\lceil n/3\rceil`$. **Dependencies:** M19–M20, M22. **Connection and role:** The exact obstruction becomes a witness that can be bounded in norm. **Sources:** [functional definition](../science/noise.md#coefficient-functional-and-its-norm).

<a id="m24"></a>
### M24 — Control the witness uniformly in copy number

**Question:** Why is its norm growth at most exponential rather than uncontrolled?

**Target:** Track the fixed coordinate change, coefficient one-norm, Dicke normalization, and singular-value decomposition in the functional estimate. **Dependencies:** M08, M11, M23. **Connection and role:** Fixed geometry yields a fixed base raised to $`n`$, which becomes an additive constant in an exponent. **Sources:** [norm proof](../science/noise.md#coefficient-functional-and-its-norm); Watrous §1.1.3.

<a id="m25"></a>
### M25 — Convert the witness into low-error weight

**Question:** Why must some compressed effect retain measurable leakage?

**Target:** Apply the positive-block trace-norm inequality, sum over three labels, and derive the lower bound on total low-error weight. **Dependencies:** M16, M23–M24. **Connection and role:** Approximate rather than exact support restrictions are now controlled for all POVMs. **Sources:** [leakage proof](../science/noise.md#quantitative-leakage-for-every-povm); [bridge estimate](WATROUS_BRIDGE.md#making-an-exact-obstruction-quantitative).

<a id="m26"></a>
### M26 — Turn low-error weight into a physical risk bound

**Question:** How do noisy eigenvalues and priors enter the converse?

**Target:** Bound the low-error eigenvalues, retain the minimum positive prior, and recognize why other sectors cannot cancel this contribution. **Dependencies:** M02, M05, M25. **Connection and role:** The algebraic witness becomes the uniform finite-copy lower bound for the stated experiment. **Sources:** [uniform error bounds](../science/noise.md#uniform-error-bounds); [model priors](../science/model.md#independent-mixing).

<a id="m27"></a>
### M27 — Bound the local noisy decoder and solve the trine readout

**Question:** How rare is an erroneous maximum-count label?

**Target:** Identify its binomial count, obtain the elementary tail bound, and distinguish the trine's exact classical postprocessing exponent from the quantum optimum. **Dependencies:** M13–M15, M22. **Connection and role:** This supplies the matching fixed-copy power and the attainable side of the many-copy comparison. **Sources:** [local upper](../science/noise.md#uniform-error-bounds); [trine exponent](../science/noise.md#trine-example); Watrous §1.2.2 as probability background.

<a id="m28"></a>
### M28 — Take the limits without interchanging them

**Question:** What does the coefficient one third mean, precisely?

**Target:** First explain the fixed-copy power, then take liminf and limsup in copy number at fixed noise, and only then take small noise. Explain why the fixed-noise limit remains unproved. **Dependencies:** M12, M24, M26–M27. **Connection and role:** Both quantitative sides now give the second global theorem with correct quantifiers. **Sources:** [asymptotic proof](../science/noise.md#the-asymptotic-order-of-limits); [bridge sandwich](WATROUS_BRIDGE.md#reading-the-noise-sandwich-in-the-right-order).

<a id="m29"></a>
### M29 — Compare the consequence and charge the implementation

**Question:** What changes after earlier results and all resources are credited?

**Target:** Separate the inherited local POVM and classical statistics from the new collective converse; compare the one-half log-Euclidean benchmark and account for copies, counters and ideal measurement assumptions. **Dependencies:** M09, M21, M28. **Connection and role:** This locates scientific novelty without claiming a quantum advantage or a capacity theorem. **Sources:** [related work](../references/RELATED_WORK.md); [interpretation and resources](../science/interpretation.md).

<a id="m30"></a>
### M30 — Reconstruct the complete scientific story

**Question:** Can the construction, converse, noise law, evidence, and limits be explained as one argument?

**Target:** Connect strict geometry to the local decoder, arbitrary-POVM compression to the coefficient obstruction, and controlled norm growth to the sharp low-noise coefficient. Distinguish analytical proof, finite checks, and unproved extensions. **Dependencies:** M21, M28–M29. **Connection and role:** Final synthesis of both theorems and their operational meaning, not an additional result. **Sources:** [science route](../science/README.md); [verification scope](../verification/README.md#limits); [endpoints and limits](../science/interpretation.md#endpoints-and-limits).
