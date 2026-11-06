# Proof obligations and claim boundaries

**Status: research integration, not release-ready.** The exploration proposed two headline claims. They must not be presented as certified theorems until the following quantifiers and arguments are checked.

## A. Exact adversarial threshold

Candidate statement: for a strict triple of pure qubit states, perfect exclusion after up to (t) unknown-location corruptions is possible precisely when (n\ge 3t+1).

1. State the adversary class precisely. Distinguish product replacement from arbitrary correlated replacement, and whether the adversary knows the preparation label.
2. For sufficiency, construct a *single* POVM independent of corruption positions. The suggested route uses the single-copy three-outcome exclusion POVM and a deterministic count decoder: with at least (n-t) honest reports, the true label can occur at most (t) times, so a label occurring more than (t) times can be safely excluded only after carefully checking the output convention. Derive the correct decoder without conflating identification and exclusion.
3. For necessity, prove that no global POVM works for (n\le3t). This must include coherent entangled measurements and not merely product decoders. Establish the requisite support-spanning or positive-definite operator witness for every strict triple.
4. Check (t=0), (n=3t), asymmetric triples, degenerate Bloch triangles, and orthogonal-pair endpoints.

## B. Independent noise exponent

Candidate asymptotic: (E(\delta)=\tfrac13\log(1/\delta)+O(1)) as (\delta\downarrow0).

1. Prove existence of the asymptotic exponent, or state liminf/limsup separately.
2. Give an explicit local protocol and bound its error using a valid classical large-deviation argument, with the actual confusion matrix of the strict triple.
3. Prove a uniform converse for arbitrary collective POVMs. A fixed-(n) Taylor coefficient alone does not imply an asymptotic exponent.
4. Verify constants in (O(1)) are uniform in the required asymptotic order and state dependence on ensemble geometry and priors.
5. Compare the sharp result with existing quantum state exclusion exponents and their regularized bounds under exactly matched hypotheses.

## C. Numerical verification

For representative strict and asymmetric triples, solve the finite-copy exclusion SDP at small (n), compare with the local protocol, and test noisy logarithmic slopes. The finite SDP does not prove a uniform asymptotic law.

## D. Novelty and significance

Attribute single-copy antidistinguishability, standard quantum exclusion error bounds, and classical large-deviation tools. Explain why the full-measurement converse is not already supplied by a prior regularized formula. Assess the actual restricted-repetition consequence under PRX Quantum's exceptional-advance/connection/insight criteria. No journal-readiness claim follows merely from a correct threshold.
