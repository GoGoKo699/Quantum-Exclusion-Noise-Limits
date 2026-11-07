# Scientific reading route

The source repeats one known member of a strict pure-qubit triple. The receiver must output a label different from that preparation. The account proves an exact corruption threshold and then quantifies how independent preparation noise prevents zero error.

## Read in dependency order

| Stage | Scientific question and result |
|---|---|
| [Model](model.md) | Define the excluded label, strict geometry, allowed error subspaces, noisy hypotheses, priors and resources. |
| [Adversarial theorem](adversarial.md) | A local count decoder attains the threshold. Symmetric compression and polynomial completeness prove that no joint measurement improves it. |
| [Uniform noise theorem](noise.md) | A norm-controlled coefficient functional yields a finite-copy risk sandwich and the leading coefficient of both asymptotic rates. |
| [Interpretation](interpretation.md) | Separate local attainability from finite-noise optimality, compare the general divergence bound, and examine an orthogonal-pair boundary. |

The [primary-source comparison](../references/RELATED_WORK.md) identifies inherited ingredients. The [verification guide](../verification/README.md) states exactly what the finite computations check. The [Watrous learning route](../learning/README.md) introduces the mechanism through a four-copy trine experiment and connects it to the complete proofs.

## Claim-to-proof map

**Exact threshold:** [local construction](adversarial.md#local-construction) plus [the coefficient obstruction](adversarial.md#why-the-relation-cannot-hold-below-the-threshold). Both use the same corruption and output convention.

**Fixed-copy noise power:** the [uniform lower and local upper bounds](noise.md#uniform-error-bounds), with the number of copies held fixed as noise vanishes.

**Many-copy low-noise coefficient:** the [functional norm bound](noise.md#coefficient-functional-and-its-norm), [positive leakage](noise.md#quantitative-leakage-for-every-povm), and [ordered limiting argument](noise.md#the-asymptotic-order-of-limits). The fixed-nonzero-noise limit is not assumed.

**Geometric boundary:** the independent [orthogonal-pair argument](interpretation.md#an-orthogonal-pair-boundary), under the same convention that output effects may be zero.

The complete contribution concerns raw repeated preparations of a fixed strict triple and ideal downstream measurements. It is not an arbitrary-noise correction theorem, an encoding capacity, or a claim that local readout is always exactly optimal.
