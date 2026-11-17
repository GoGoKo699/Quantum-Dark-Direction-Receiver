# What receiver calibration must distinguish

Depolarizing storage preserves the mean eigenray used by the global estimator. Coherent memory errors need not do so. Two exact limitations show why the [positive noise theorem](memory-noise.md) and [paid scalar calibration](calibration.md) have deliberately stated models.

## An exchange ambiguity for parity readouts

Every parity/tensor-square/wedge effect in [the receiver](receiver.md) commutes with physical SWAP. Suppose the first stored specimen undergoes an unknown fixed unitary $`U`$, and the second specimen is fresh. The input is then

```math
\rho_{Uf}\otimes\rho_f.
```

Choose distinct rays $`f,h`$ and a unitary with $`Uf=h`$. The two worlds

```math
\begin{array}{c|c|c}
\text{target}&\text{memory}&\text{pair input}\\ \hline
f&U&\rho_h\otimes\rho_f\\
h&U^\dagger&\rho_f\otimes\rho_h
\end{array}
```

give identical probabilities for every SWAP-commuting effect. This persists for arbitrary classical adaptation among such effects: induction over the complete history gives identical transcript laws. No number of these pair records can identify which ray was the fresh target.

For any reported ray $`a`$, the average loss at the two targets is at least

```math
1-\lambda_{\max}\left(\frac{P_f+P_h}{2}\right)
=\frac{1-|\langle f|h\rangle|}{2}.
```

Thus an allowed residual coherent angular uncertainty $`\beta`$ can force a floor $`(1-\cos\beta)/2`$, approximately $`\beta^2/4`$. A target $`O(1/N)`$ risk requires angular uncertainty of order $`N^{-1/2}`$, or an additional order-sensitive measurement/reference that breaks the ambiguity.

This is a theorem about the stated SWAP-commuting pair architecture and a coherent-unitary memory slice. A separately measured fresh specimen, nonsymmetric effects, or independent references can break its premise. It is not a no-go for every conceivable two-copy receiver, nor does it automatically extend to a mixture with known depolarization. The specimen cost of learning a unitary depends on allowed probes, entanglement and repeated coherent access; no universal calibration coefficient is inferred.

## Entanglement-breaking storage gives a finite simulation

For the qutrit depolarizing channel, $`0\le\nu\le1/4`$ admits an explicit measure-and-prepare representation. Let $`P_\ell`$ be the twelve MUB ray projectors and set

```math
F_\ell=\frac14P_\ell,\qquad
\sigma_{\nu,\ell}=4\nu P_\ell+(1-4\nu)I/3.
```

The prepared matrices are density operators in this range. The 2-design identity gives

```math
\mathcal D_\nu(T)
=\sum_\ell\mathrm{tr}(F_\ell T)\sigma_{\nu,\ell}.
```

For any joint effect $`E_y`$ on stored-first plus fresh-second, a one-copy strategy can measure $`F_\ell`$ on the first specimen, store its classical result, prepare the known ancilla $`\sigma_{\nu,\ell}`$, and induce the conditional second-specimen POVM

```math
G_{y|\ell}=\mathrm{tr}_1[
(\sigma_{\nu,\ell}^{1/2}\otimes I)E_y
(\sigma_{\nu,\ell}^{1/2}\otimes I)].
```

It reproduces the complete pair outcome distribution using the same two unknown-source specimens. Adaptation and subsequent processing are preserved. Therefore no receiver forced through this storage channel can beat the full adaptive one-copy class at any finite budget in this parameter range. This uses the established entanglement-breaking measure-and-prepare principle; [related work](../references/RELATED_WORK.md) credits that framework.

The simulation is pointwise in the physical parameter, and the ideal comparator may be supplied that parameter. It gives no sharp transition above $`1/4`$. The moment estimator's approximately $`0.823`$ asymptotic crossing and the finite sufficient visibility ranges are different statements and must not be read as universal impossibility thresholds.

## Operating assumptions that remain explicit

The positive account charges every reference specimen, failed calibration and rejected branch. It still assumes the exact source promise, stable independent uses of the specified memory, accurate known reference preparation, and declared bounds on laboratory controls/readout. A finite scalar calibration test does not certify these structural assumptions. Arbitrary drift, source leakage, unknown frame rotations and correlated detector faults require different likelihoods and budgets.

The established benefit is a number-of-specimens comparison. One stored qutrit, entangling readout, control precision and reference-source construction may cost more laboratory time or hardware than separate measurements. Those costs are stated rather than converted into an unproved practical advantage.
