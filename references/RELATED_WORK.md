# Prior results and the robustness contribution

The task is exclusion: an error is outputting the actual preparation label. The receiver gets repeated copies of one fixed hypothesis, not a string of independently chosen labels. The full operational assumptions are in [the model](../science/model.md). The comparisons below concern the cited versions, inspected on 7 November 2026 (Singapore time).

## One-copy qubit exclusion

Heinosaari and Kerppo, *Antidistinguishability of Pure Quantum States*, [arXiv:1804.10457v2](https://arxiv.org/abs/1804.10457v2), Proposition 6 and equations (17)--(20), give the positive-weight qubit criterion and the orthogonal-complement POVM used here. Their discussion credits the earlier qubit characterization to Caves, Fuchs and Schack. The strict Bloch triangle and the effects $`F_i=c_i|\phi_i\rangle\langle\phi_i|`$ are inherited inputs, not new discoveries.

Their definition requires every label to occur for some input. Our minimum-error model permits zero effects. This distinction matters for the orthogonal-pair boundary control, which can discard the third output label. The strict-triple construction uses all three labels, and its converse allows the larger measurement class.

## Classical and quantum error exponents

Mishra, Nussbaum and Wilde, *On the optimal error exponents for classical and quantum antidistinguishability*, [arXiv:2309.03723v2](https://arxiv.org/abs/2309.03723v2), establish the classical multivariate Chernoff exponent and quantum bounds. We use the classical result only for interpreting a fixed local measurement; the trine formula also has a direct type proof in [the noisy account](../science/noise.md#trine-example). An exact classical exponent does not provide an upper bound against arbitrary collective quantum measurements.

## The closest general collective converse

Ji, Mishra, Mosonyi and Wilde, *Barycentric bounds on the error exponents of quantum hypothesis exclusion*, [arXiv:2407.13728v4](https://arxiv.org/abs/2407.13728v4), Theorem 15, equation (129), upper-bound the quantum limsup exponent by the multivariate log-Euclidean Chernoff divergence. Proposition 17, equations (144)--(151), identifies their regularized extended-Renyi bound with that same single-letter quantity.

For the present strict triples, our [explicit evaluation](../science/interpretation.md#comparison-with-the-general-divergence-converse) is $`-\log[2\sqrt{\delta(1-\delta)}]`$, with small-noise coefficient $`1/2`$. The coefficient-functional converse proves $`1/3`$ instead. Thus neither the displayed general bound nor that particular regularization implies the present sharp coefficient. This does not claim to exclude every possible divergence-based method.

## Ideal pure-state many-copy results

Diebra, Llorens, Bagan, Sentis and Munoz-Tapia, *Quantum state exclusion for group-generated ensembles of pure states*, [arXiv:2503.02568v2](https://arxiv.org/abs/2503.02568v2), solve ideal group-generated pure-state exclusion through Gram-spectrum criteria and constructions. Their pure-state formulas do not directly apply to the mixed tensor-power hypotheses or the error subspaces here. Our asymmetric triples also need not be group-generated.

Roy, Gupta, Ghosal, Sen and Bandyopadhyay, *Quantum state exclusion with many copies*, [arXiv:2601.14410v2](https://arxiv.org/abs/2601.14410v2), prove finite-copy activation for three or more pure states, with sets requiring arbitrarily many copies. Those statements concern ideal repeated pure states and require nontrivial use of every output label. In this project the ideal strict triples already permit one-copy exclusion; the question is how corruption removes it, and how fast a residual error can decrease.

## What is additional here

The local construction combines the known qubit POVM with counting and a pigeonhole argument. The new load-bearing step is the converse for every joint POVM: symmetric compression turns zero error into polynomial divisibility, and a coefficient of the identity prevents completeness below $`n=3t+1`$. Its norm-controlled version gives a lower bound uniform in $`n`$, proving the sharp $`1/3`$ coefficient for both lower and upper asymptotic rates. The fixed-$`n`$ power $`\lceil n/3\rceil`$ is a consequence of the same bounds.

The contribution is restricted to raw repetition of strict pure-qubit triples and the declared noise models. It does not solve the general fixed-noise quantum exclusion exponent, or claim optimality of local measurements at every noise strength. The exact boundary comparison uses established binary testing ingredients. The search and these matched-model comparisons support the stated distinction; they are not an exhaustive priority certificate.

Full citation metadata are in [references.bib](references.bib).
