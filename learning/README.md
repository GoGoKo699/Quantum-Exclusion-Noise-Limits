# Learn quantum exclusion under preparation noise

A source chooses one of three known qubit states and sends repeated preparations. The receiver does not have to identify the state. It must name one state that was **not** prepared. This different decision rule is the starting point of the project.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the author's [standard-layout manuscript](https://jhwatrous.github.io/TQI.pdf). The [source bridge](WATROUS_BRIDGE.md) gives selected sections, notation translations, and the project-specific steps that the book does not contain. No second textbook is required.

## One complete experiment

Consider the three equatorial states with phases $`z_j=e^{2\pi\mathrm{i}j/3}`$, called the trine. Measure one qubit with the three effects

```math
F_j=\frac23|\phi_j\rangle\langle\phi_j|,
\qquad \langle\phi_j|\psi_j\rangle=0.
```

For an ideal input with label $`i`$, the measurement never reports $`i`$ and reports each other label with probability one half. Its outcome is therefore an excluded label, not an estimate of the prepared label.

Now take **four** preparations and allow **one** arbitrary corruption at an unknown location. Apply that measurement to each qubit and count the outcomes. The true label can appear at most once. Some label must appear at least twice because four outcomes are distributed among three counters. Output a maximum-count label: it cannot be the true one.

For example, counts $`(2,1,1)`$ permit output 0; counts $`(0,2,2)`$ permit output 1 or 2. No outcome is discarded. Four local measurements and three counters suffice, with no coherent memory between copies. The proof also covers coherent error-location superpositions, as explained in the [bridge](WATROUS_BRIDGE.md#from-individual-records-to-coherent-errors).

With three copies and one corruption, the record $`(1,1,1)`$ leaves this counting rule without a safe conclusion. That observation only defeats the rule. Proving that **every joint quantum measurement** fails is the separate, central converse.

## Follow one route

The [30-milestone map](MILESTONES.md) has **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The background joins states, positive measurements, error subspaces, symmetry and polynomial notation into one precise experiment. The narrative joins the local construction to the global converse, then converts the exact obstruction into a uniform noisy bound.

Start with this example, use the [Watrous bridge](WATROUS_BRIDGE.md) when a concept is unfamiliar, and follow [M01 through M30](MILESTONES.md#m01). Readers ready for the theorem can go directly to the [scientific reading route](../science/README.md).

The map describes understanding targets and their dependencies, not a learner's progress or a quiz. The detailed proofs remain in their scientific homes; the learning pages explain how to reach them.

## Keep three claims distinct

The [adversarial theorem](../science/adversarial.md) is an exact zero-error threshold. The [finite-copy noise theorem](../science/noise.md#uniform-error-bounds) fixes the number of copies and identifies a small-noise power. The [asymptotic theorem](../science/noise.md#the-asymptotic-order-of-limits) first lets the number of copies grow at fixed noise, then controls the leading small-noise coefficient of both lower and upper exponent rates. Neither a fixed-noise limit nor exact finite-noise optimality of the local decoder follows from these statements.
