# Finding the direction the source never occupies

Imagine three distinguishable laboratory modes. A device emits one qutrit at a time, always inside some two-dimensional plane and equally spread over that plane. The remaining direction is empty. The plane can point anywhere, so the receiver must discover the empty ray rather than verify a supplied guess.

The promise is precise: each specimen has state $`\rho_f=(I-P_f)/2`$. Here $`P_f`$ is the projector onto the unknown empty ray. The example uses exact rank two and equal occupied populations. The ideal collective calculation also works for a uniformly occupied hyperplane in any finite dimension. The pair receiver and paid calibration below use the qutrit source.

## Start with one orientation we can see

For a worked example, suppose the true empty ray happens to be $`f=e_0`$. The receiver is not told this. In the laboratory basis its source is

```math
\rho_{e_0}=\begin{pmatrix}0&0&0\\0&1/2&0\\0&0&1/2\end{pmatrix}.
```

A direct basis measurement can therefore report modes one or two, never mode zero. That observation would be useful if the empty direction were one of the three basis vectors. In the actual task it can be any complex superposition. The receiver must distinguish all those rays, and it is allowed to rotate its measurements or adapt them using earlier results.

A reported ray is scored by $`1-|\langle\widehat f|f\rangle|^2`$. Reporting the true ray costs zero; an orthogonal ray costs one. A small mean loss means the output usually points close to the empty direction. The theorem asks for a guarantee at the **worst** true ray, averaging over every outcome and every random setting.

## Let two specimens meet

Store the first qutrit until the second arrives. Their joint input is still a product of two independent mixed states. For $`f=e_0`$, its four equally weighted basis components are $`|11\rangle,|12\rangle,|21\rangle,|22\rangle`$.

SWAP exchanges the two registers. The pair can be split into symmetric and antisymmetric subspaces. The mixed part involving $`|12\rangle`$ and $`|21\rangle`$ contains both

```math
\frac{|12\rangle+|21\rangle}{\sqrt2}
\quad\text{and}\quad
\frac{|12\rangle-|21\rangle}{\sqrt2}.
```

The whole symmetric branch occurs with probability $`3/4`$. The antisymmetric branch occurs with probability $`1/4`$, and its normalized state is the **pure** wedge $`e_1\wedge e_2`$. That wedge describes the occupied plane. In three dimensions it also identifies the orthogonal missing ray, through the conjugate Hodge map

```math
g(f)=(\overline f_2,-\overline f_1,\overline f_0)
```

in wedge basis $`(e_0\wedge e_1,e_0\wedge e_2,e_1\wedge e_2)`$. In our example $`g(e_0)=(0,0,1)`$, the last wedge-basis vector.

This does not mean one quarter of the trials supplies a free known pure state. A receiver must still measure that unknown pure wedge, and each attempt has already consumed two specimens. The symmetric branch also contains information and remains part of the record. Discarding it or counting only the successful antisymmetric events would change the resource comparison.

## See all twenty-four outcomes in the toy example

The small-budget apparatus reads each parity branch using the twelve rays from four qutrit mutually unbiased bases. Those twelve rays contain the three laboratory vectors and nine equal-magnitude superpositions. The apparatus therefore has twelve symmetric labels and twelve antisymmetric labels.

An antisymmetric label $`\psi`$ is expressed in dark-ray coordinates: its physical wedge effect acts on $`g(\psi)`$. This convention makes it meaningful to compare its label with the later single-qutrit label.

For $`f=e_0`$, let $`u=|\langle\psi|e_0\rangle|^2`$ denote the squared ray overlap. The following table gives the probability of **each** label in its row:

| Dark-space label $`\psi`$ | Number of labels | $`u`$ | Symmetric outcome | Antisymmetric outcome |
|---|---:|---:|---:|---:|
| $`e_0`$ | 1 | $`1`$ | $`0`$ | $`1/16`$ |
| $`e_1`$ or $`e_2`$ | 2 | $`0`$ | $`1/8`$ | $`0`$ |
| An equal-magnitude MUB superposition | 9 | $`1/3`$ | $`1/18`$ | $`1/48`$ |

The symmetric column sums to $`3/4`$ and the antisymmetric column to $`1/4`$. Every probability belongs to the same two-specimen experiment. The [receiver proof](../science/receiver.md) constructs the effects and verifies their sum is the identity.

One pair is already informative, but that is different from beating every separate-measurement strategy. At total budget two, the exact minimax risk is $`23/40`$ for **both** unrestricted collective measurements and adaptive one-copy measurements. Even a more elaborate joint apparatus cannot improve that value under this source and loss.

## The third specimen changes the comparison

Measure the third specimen separately and combine its label with the full pair record. For the finite MUB apparatus, both labels are rays in the same dark-space coordinates. The decision rule computes an unnormalized posterior ray matrix and returns one of its leading eigenvectors. The matrix is an average of possible target projectors weighted by the observed likelihood; maximizing its expectation of the guessed projector maximizes conditional fidelity for that averaging rule. Haar weighting is a mathematical tool for designing the rule; the actual unknown ray remains fixed across all specimens.

For example, suppose the pair reports the antisymmetric label $`A=P_{e_0}`$, and the third specimen reports $`B=P_{e_1}`$. These labels are orthogonal. The relevant posterior matrix is proportional to

```math
4I+4P_{e_0}-P_{e_1}
=\mathrm{diag}(8,3,4).
```

Its leading eigenray is $`e_0`$. Under the toy true ray, that complete record occurs with probability $`(1/16)(1/8)=1/128`$. The decision rule points in the right direction for this record without being supplied the true ray.

The symmetric branch can also help. If its label is $`A=P_{e_1}`$ and the third label is $`B=P_{e_2}`$, the posterior matrix is proportional to

```math
52I-28P_{e_1}-20P_{e_2}
=\mathrm{diag}(52,24,32).
```

It again selects $`e_0`$. That complete record has probability $`1/64`$ in the toy example. Other records can produce imperfect answers; the guarantee includes their weighted losses as well. These two favorable examples illustrate the rule, not its proof or its overall success rate.

The base MUB apparatus has orientation-dependent performance. A common independent known laboratory rotation is therefore applied to the pair readout, the third-specimen readout and the reported ray. Haar averaging makes its risk the same at every true direction. A finite setting algorithm with 2304 fair random bits approximates that averaging with a uniform error bound, includes its conditioning fallback and requires stated physical control tolerances. It does not assume an exact Haar sample from finitely many bits.

These are the risks of the worked pair receivers and the lower bound that covers every adaptive single-copy receiver.

| Three-specimen receiver | Worst-case expected infidelity |
|---|---:|
| Continuous covariant pair-plus-single receiver | $`1907/3600\approx0.529722`$ |
| Ideal MUB pair-plus-single readout with common Haar setting | About $`0.530124`$ |
| Explicit finite setting and the stated control-error budget | Below $`0.531375`$ |
| Every adaptive one-copy protocol | At least $`0.53735011`$ |

The last row is not the performance of one selected tomography algorithm. Every adaptive one-copy history induces a product of positive effects. Such effects satisfy a positivity condition after transposing any specimen register. Enlarging the comparator to that larger PPT class makes the lower-bound problem easier. An explicit rational dual certificate bounds even that enlarged class. The exact verifier checks the certificate; a numerical optimizer only guided its discovery. The [finite-budget proof](../science/finite-budget.md) provides the full reduction and qualification that the precise one-copy optimum is still unknown.

## What all three specimens can do together

Keep all three qutrits until the receiver can measure them jointly. The equality of the specimens lets us decompose the tensor power into subspaces distinguished by how the registers transform under permutations. Give each subspace its own decision rule. The [collective proof](../science/collective-minimax.md) finds the best fidelity in every such subspace by asking which measurement effects place zero population on the guessed missing ray.

At three specimens, the fully symmetric sector and the mixed-symmetry sector each receive probability $`1/2`$. Their best conditional fidelities are $`5/12`$ and $`8/15`$. The fully antisymmetric sector receives zero probability because the specimens all lie in a two-dimensional plane. The total best fidelity is $`(5/12+8/15)/2=19/40`$, so the exact infidelity is $`21/40`$.

That zero-probability sector still matters. A measurement must sum to the identity on the entire three-qutrit register. An effect that factors across a pair and a single qutrit can cover the fully antisymmetric sector only by also using directions that lower the score. This is why the best pair-plus-single measurement falls short of fully joint readout.

| Three-specimen measurement access | Minimax infidelity |
|---|---:|
| Fully joint POVM | $`21/40=0.525000`$, exact |
| POVM whose individual effects are biseparable | $`1-25/64-\sqrt{6001}/960\approx0.528681`$, exact |
| Sequential pair and single in either order, or complete fixed-cut separable POVMs | $`1-83/192-3\sqrt{17}/320\approx0.529054`$, exact |
| Adaptive single-copy measurement | At least $`0.53735011`$ |

In the second row, each effect may use a mixture of bipartitions. In the third row, each complete fixed-cut POVM uses the same bipartition for every effect. Randomizing among complete fixed-cut POVMs gives the same optimum. Either order of the sequential implementation attains that value. The [measurement hierarchy proof](../science/measurement-hierarchy.md) separates these cases and constructs the attaining effects.

In dimension $`d\ge3`$, separate measurements match the collective optimum through $`d-1`$ specimens. A ray perpendicular to all the observed rank-one outcome vectors attains the score bound. At $`d`$ specimens, the fully antisymmetric sector again forces a loss for any measurement whose effects are biseparable. This identifies the first budget at which fully joint access helps in the ideal model.

## Why Fisher information is not the finish line

The selected review explains local information and covariance bounds alongside global statistical methods. Here it is useful to keep three different questions separate: how sensitively probabilities change near a chosen ray, how a rule performs with the observed finite record, and how much laboratory calibration that rule requires.

In the local angular convention, one mixed source specimen has SLD QFI $`2I_4`$, and an independent pair has $`4I_4`$. The [one-copy proof](../science/one-copy-bound.md) also bounds each actual one-copy measurement's classical information trace by two. Those facts guide the mathematics. They do not establish the three-specimen risk numbers above. Exact finite decision calculations and the full-comparator certificate supply that step.

## Pay for checking the memory

For many specimens, a second receiver uses a fixed 450-outcome pair measurement. Each record contributes a small Hermitian matrix, and the estimate is the leading eigenray of their average. The first stored qutrit is assumed to pass through an independent stationary depolarizing channel with unknown strength $`\nu`$; the second is fresh. Under this particular channel, the mean score remains a positive multiple of $`P_f`$ plus an identity shift. The target eigenray therefore survives without first fitting $`\nu`$.

To check a useful operating range, send known pure reference pairs through that same memory and receiver. Their antisymmetric probability is $`(1-\nu)/3`$. For 100,000 reference pairs, accept if at most 500 antisymmetric outcomes are observed. At $`\nu=0.99`$, the ideal expected count is about 333; at $`\nu=0.98`$, it is about 667. Exact finite binomial bounds quantify rejection and false acceptance, including the declared readout tolerance.

The full ledger is 200,000 reference specimens plus 2.8 million unknown-source specimens. All signal pairs are measured even when calibration rejects, and the fallback on rejection contributes to unconditional risk. Under the declared good-memory and control assumptions, the certified pair risk is below $`2.596812\times10^{-6}`$. Every adaptive one-copy protocol has risk above $`2.666652\times10^{-6}`$ even when granted all three million specimens as ideal signals.

This is a specimen advantage after **scalar memory calibration** is paid. The same parity test does not validate the depolarizing model, establish source stationarity, calibrate reference preparation or learn arbitrary receiver errors. The uniform readout-error bound is a separate explicit assumption. Unknown coherent memory rotation can even make the SWAP-parity architecture ambiguous between two target rays; [the limitations](../science/limits.md) show that exact obstruction.

## Put the whole result together

The ideal calculation gives the exact collective minimax risk at every specimen budget. Three qutrits already separate fully joint access, biseparable effects, sequential pair access and separate readout. The larger fixed pair receiver establishes a different guarantee under its stated memory and paid calibration contract. [Related work](../references/RELATED_WORK.md) credits the earlier collective measurement architecture, matrix estimator and PPT methods.

The experiment still needs storage, joint control, ancillas, calibrated tolerances and a reference source. Saving specimens does not prove lower laboratory time, energy or hardware expense. The [30-milestone map](MILESTONES.md) connects those boundaries to the mechanism and proofs; the [anchor bridge](ANCHOR.md) identifies the foundations supplied by the selected review.
