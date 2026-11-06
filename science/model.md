# State exclusion with preparation corruption

## Experiment

Let (H=\mathbb C^2) and let ({|psi_i\rangle:i=1,2,3}) be three distinct pure qubit states. The receiver is given (n) systems, all nominally prepared in one unknown member of this ensemble. The receiver outputs an index (j) that must **not** equal the actual preparation index (i).

An exclusion measurement is a POVM ({M_j}_{j=1}^3), with (M_j\succeq0) and (sum_jM_j=I). For hypotheses (ho_i), its average exclusion error under prior (p_i>0) is
[
 P_{\mathrm{err}}=\sum_i p_i\operatorname{Tr}(M_i\rho_i).
]
Perfect exclusion means each term vanishes. It is not ordinary minimum-error identification.

## Independent mixing

Fix (0<\delta<1/2), and define
[
 \rho_i(\delta)=(1-\delta)|\psi_i\rangle\langle\psi_i|
 +\delta|\psi_i^\perp\rangle\langle\psi_i^\perp|.
]
The receiver gets (ho_i(\delta)^{\otimes n}) and may make any collective POVM. Write (P_n^*(\delta)) for the optimum average exclusion error. Define the asymptotic exponent, when the limit exists, by
[
 E(\delta)=\lim_{n\to\infty}-\frac1n\log P_n^*(\delta).
]
All results must distinguish a fixed-(n) small-(\delta) expansion from the (n\to\infty) exponent and its subsequent (\delta\downarrow0) limit.

## Adversarial corruption

An adversary may replace up to (t) of the (n) nominally identical preparations by arbitrary qubit states, possibly with unknown locations. Specify whether corruption is independent, correlated, or entangled with an external register before making a theorem claim. A universal zero-error guarantee requires a single measurement valid for all allowed corrupted preparations.

## Ensemble geometry

A strict triple means the origin is in the interior of the triangle formed by the three Bloch vectors. This is equivalent to strictly positive weights (w_i) with (sum_iw_i=1) and (sum_iw_i\mathbf r_i=0). For the ideal one-copy ensemble, the effects (M_i=2w_i|\psi_i^\perp\rangle\langle\psi_i^\perp|) sum to (I) and perfectly exclude the respective hypotheses.

## Resource contract

All supplied copies count. No preparation oracle, inverse state-preparation unitary, environmental error flag, error-location label, or free postselection is assumed. Classical computation and the final joint POVM are unrestricted; a concrete local attaining construction, if established, should also account for its classical processing. This model does not assert a hardware-efficient implementation of an arbitrary collective POVM.
