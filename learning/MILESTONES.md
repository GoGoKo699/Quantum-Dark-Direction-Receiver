# Thirty milestones from a missing ray to a finite receiver

This is the project's common understanding map. Its single educational anchor is Demkowicz-Dobrzański, Górecki and Guţă, *Multi-parameter estimation beyond Quantum Fisher Information*, [arXiv:2001.11742v2](https://arxiv.org/abs/2001.11742v2), published in J. Phys. A **53**, 363001 (2020). The [anchor bridge](ANCHOR.md) translates its estimation language into the missing-ray model, with rank-two qutrits as the worked example.

The map has **12 background/preliminary milestones** and **18 narrative/innovation milestones**. The background connects physical states, measurement records, risk and symmetry into one complete comparison framework. The narrative builds the pair mechanism, exact collective formula and three-specimen hierarchy. It then closes the resource ledger for a noisy pair receiver. This allocation leaves the specialist algebra in the scientific sources while making the contribution understandable as one story.

Each milestone is a conceptual target, rather than a claim to cover every technical lemma. Dependencies refer to earlier targets; source pointers identify the authoritative statements. Anchor sections supply foundations and context. The exact collective score, qutrit hierarchy, rational PPT certificate and paid calibration proofs are developed in this repository with the research dependencies credited in the scientific account.

## Background and preliminaries: M01–M12

### M01 — A direction without a physically meaningful phase

**Central question:** What does it mean to identify a ray rather than a particular vector?

**Understanding target:** Explain why multiplying a normalized state vector by a common phase changes its coordinates but not its physical ray, and why a rank-one projector represents the target without that ambiguity.

**Dependencies and story role:** None. This starts with the local physical object the receiver must report.

**Conceptual connection:** A direction in three complex levels is the output object; the target is not a list of arbitrary preparation amplitudes.

**Source pointers:** Anchor §1.2 for parameterized states and estimated quantities; [input, output and loss](../science/model.md#input-output-and-loss).

### M02 — A filled plane hides its missing direction

**Central question:** What is promised by a source that occupies two levels equally and leaves one ray empty?

**Understanding target:** Relate the missing-ray projector to its orthogonal occupied plane. Distinguish the exact rank-two, equal-population promise from a general mixed qutrit or a device with a merely weak response.

**Dependencies and story role:** M01. It connects the target ray to the actual specimens carrying information about it.

**Conceptual connection:** The unknown direction is encoded through an absence, while the occupied subspace has no preferred basis. The same uniform hyperplane promise defines the ideal problem in any finite dimension.

**Source pointers:** Anchor §1.2; [promised source](../science/model.md#input-output-and-loss).

### M03 — Scoring a reported direction

**Central question:** How can two candidate rays be compared without depending on their chosen phases?

**Understanding target:** Interpret dark-ray infidelity as zero for the correct ray and one for an orthogonal ray. Explain why this loss differs from infidelity between two mixed qutrit preparations.

**Dependencies and story role:** M01–M02. It turns a physical target into the task's precise penalty.

**Conceptual connection:** The reported ray and the missing ray determine the score; errors in unrelated state coordinates are not silently substituted for that score.

**Source pointers:** Anchor §1.2 for the role of a cost function; [ray loss](../science/model.md#input-output-and-loss).

### M04 — A measurement produces a complete classical record

**Central question:** What information is actually available after a quantum measurement?

**Understanding target:** Connect POVM effects to outcome probabilities and distinguish the physical measurement from the classical estimator applied afterward. Identify settings, branch labels and final outcomes as parts of the complete record.

**Dependencies and story role:** M02–M03. It introduces the interface between specimens and a reported answer.

**Conceptual connection:** A receiver is evaluated using all recorded outcomes; a rare successful branch cannot be treated as a free replacement source.

**Source pointers:** Anchor §1.2 and §5.2; [measurement classes](../science/model.md#measurement-classes) and [receiver labels](../science/receiver.md#registers-and-outcome-labels).

### M05 — Independence and the specimen ledger

**Central question:** Which attempts consume the finite budget?

**Understanding target:** Explain what independent identical signal specimens mean here. Count both members of a pair, every pilot and every known-reference preparation, including uses that later lead to rejection or fallback.

**Dependencies and story role:** M04. It adds the experiment's resource accounting before any advantage comparison.

**Conceptual connection:** More useful information per retained outcome is not necessarily more useful information per prepared specimen.

**Source pointers:** Anchor §1.2 for the repeated experiment; [total specimen accounting](../science/model.md#total-specimen-accounting).

### M06 — What one-copy adaptation can and cannot retain

**Central question:** What extra resource separates a pair receiver from the full adaptive one-copy class?

**Understanding target:** Allow arbitrary one-copy POVMs, fresh ancillas and the entire classical history, while recognizing the prohibition on coherent information linking unknown specimens. Explain why one stored qutrit changes that access model.

**Dependencies and story role:** M04–M05. It fixes the separate-readout comparator and the resource that a joint block adds.

**Conceptual connection:** The distinction concerns coherent measurement access, rather than a comparison with one selected tomography algorithm.

**Source pointers:** Anchor §2.10 for the role of multiple-copy measurements; [measurement classes](../science/model.md#measurement-classes).

### M07 — Risk includes every way the experiment can end

**Central question:** What does worst-case expected infidelity require beyond an accurate typical outcome?

**Understanding target:** Separate an outcome's loss, its expected loss at a fixed true ray, and the largest such expectation over all rays. Include random settings, estimator bias, rejected calibration and fallback outputs in the expectation.

**Dependencies and story role:** M03–M06. It assembles the performance criterion for the complete allowed experiment.

**Conceptual connection:** A guarantee for a wholly unknown direction must control unfavorable orientations and failure events, not only a supplied local neighborhood.

**Source pointers:** Anchor §1.2; [risk definition](../science/model.md#input-output-and-loss) and [unconditional calibration risk](../science/calibration.md#signal-estimator-and-unconditional-risk).

### M08 — An average can bound a worst case

**Central question:** Why can a Haar average help analyze a minimax task whose true ray is wholly unknown?

**Understanding target:** Explain why each strategy's largest risk is at least its average under any chosen prior. Distinguish a mathematical prior used in a converse from orientation information supplied to the physical receiver.

**Dependencies and story role:** M07. It provides the first bridge from an all-orientations task to a tractable integral.

**Conceptual connection:** Bayesian analysis can certify a minimax lower bound without changing the operational input promise.

**Source pointers:** Anchor §§5.2–5.3; [finite converse](../science/finite-budget.md#3-a-certificate-covering-every-adaptive-one-copy-strategy).

### M09 — Covariance removes a preferred orientation

**Central question:** When does a known common random rotation turn an average performance into a uniform one?

**Understanding target:** Track the coordinated rotation of inputs, measurement effects and reported ray. Explain why averaging the whole protocol preserves its mean fidelity and makes its ideal risk independent of the true orientation.

**Dependencies and story role:** M01, M04, M08. It connects a local choice of laboratory coordinates to a global unknown-ray guarantee.

**Conceptual connection:** The random setting is known to the receiver and independent of the source; it is not a supplied estimate of the unknown dark direction.

**Source pointers:** Anchor §5.3; [two-specimen attainability and twirling](../science/finite-budget.md#1-exact-equality-at-two-specimens).

### M10 — Local sensitivity is not a finite-risk theorem

**Central question:** What is learned from Fisher information, and what still needs proof at a fixed specimen budget?

**Understanding target:** Distinguish a derivative-based local sensitivity statement from a global loss bound for a finite experiment. Explain the roles of unbiasedness, regularity, asymptotic limits and possible failure events.

**Dependencies and story role:** M07–M09. It prevents an appealing large-sample coefficient from being mistaken for the requested finite comparison.

**Conceptual connection:** Information bounds remain useful ingredients, but the contribution needs an estimator and a finite risk inequality matched to the same task.

**Source pointers:** Anchor §§2.1–2.2, 2.11, 5.5 and 6; [global one-copy bound](../science/one-copy-bound.md) and [finite receiver risk](../science/memory-noise.md#finite-risk-including-large-errors).

### M11 — A relaxed measurement class can certify a converse

**Central question:** How can one bound every adaptive one-copy protocol without enumerating its possible decision trees?

**Understanding target:** Understand the direction of a relaxation: a larger class can only improve the best attainable fidelity. Relate positive semidefinite inequalities and a feasible dual certificate to an upper bound on that larger class's fidelity.

**Dependencies and story role:** M06, M08. It introduces the logic needed to read the exact PPT certificate without treating a numerical optimum as proof.

**Conceptual connection:** Fully separable effects from complete one-copy histories lie inside the PPT relaxation used in the project. The relaxation and its rational certificate are specialist ingredients supplied locally.

**Source pointers:** Anchor §2.4 for optimization context, rather than the project's PPT theorem; [complete histories to a PPT seed](../science/finite-budget.md#from-complete-histories-to-a-ppt-seed) and [rational dual](../science/finite-budget.md#a-rational-feasible-dual).

### M12 — One complete comparison experiment

**Central question:** Which pieces must be fixed before the words “pair advantage” have an operational meaning?

**Understanding target:** State the source promise, reported ray, loss, finite specimen ledger, permitted references and measurement classes together. Explain how an attaining protocol and a full-class lower bound must match these choices. Describe unrestricted collective access and the effect-level factorization that defines a biseparable comparator.

**Dependencies and story role:** M01–M11. This integrates the background phase into the project's complete decision problem.

**Conceptual connection:** The later mechanism, certificate and calibration theorem are different parts of one comparison, rather than interchangeable performance claims.

**Source pointers:** Anchor §1.2 and §§5.2–5.3; [full model](../science/model.md) and [prior-work boundary](../references/RELATED_WORK.md).

## Narrative and innovation: M13–M30

### M13 — The occupied plane produces a conjugate hole

**Central question:** Why is the antisymmetric part of two rank-two specimens a pure state?

**Understanding target:** Explain how antisymmetrization selects the wedge of the occupied vectors and why its three-dimensional representation identifies the missing ray through a conjugate Hodge map. Keep its one-quarter branch probability attached to that information.

**Dependencies and story role:** M02, M04–M06, M12. The narrative begins with the physical mechanism that makes pair readout useful.

**Conceptual connection:** A pure conditional description emerges from mixed inputs, but obtaining it consumes both specimens and does not erase the other branch.

**Source pointers:** Anchor §2.10 as multiple-copy context; [parity and the conjugate hole](../science/receiver.md#registers-and-outcome-labels).

### M14 — A finite receiver needs consistent outcome labels

**Central question:** How do the twelve qutrit MUB rays become a complete 24-outcome pair measurement?

**Understanding target:** Connect the design identities to completeness in both parity sectors. Explain why an antisymmetric outcome must be mapped back to its dark-space ray before comparing its overlap with the third specimen's outcome.

**Dependencies and story role:** M04, M09, M13. It turns the pair mechanism into the concrete measurement used in the small-budget theorem.

**Conceptual connection:** The Hodge map affects labels as well as states; inconsistent labels would break the finite overlap calculation.

**Source pointers:** Anchor §1.2 for POVM conventions; [24-outcome receiver](../science/receiver.md#the-24-outcome-small-budget-receiver) and [fixed finite measurements](../science/finite-budget.md#fixed-finite-quantum-measurements).

### M15 — The score ceiling in each collective sector

**Central question:** How can the same optimality argument work at two qutrits and at an arbitrary specimen budget?

**Understanding target:** Recognize that identical copies split into Schur sectors with known weights. Explain why the largest conditional score in each sector is attained on its subspace with zero occupation of the guessed ray. Use the weighted conditional fidelities to recover the qutrit risk $`23/40`$ at two specimens and $`21/40`$ at three.

**Dependencies and story role:** M04, M08–M09, M13–M14. It sets the exact benchmark for the restricted measurements.

**Conceptual connection:** The occupied-subspace projector supplies both the attaining measurement and the score-maximizing support. The Schur weighting tells how often the source reaches each case.

**Source pointers:** Anchor §§5.3–5.4 for covariant score optimization, [exact collective risk](../science/collective-minimax.md) and [two-qutrit calculation](../science/finite-budget.md#1-exact-equality-at-two-specimens).

### M16 — Separate measurements reach the ceiling up to dimension minus one

**Central question:** Why can signals that interact during readout provide no gain at the smallest budgets?

**Understanding target:** Given rank-one outcomes from separate specimens, find a guess perpendicular to all their outcome rays when the specimen count is at most $`d-1`$. Explain why each corresponding product effect lies in the score-maximizing subspace for that guess and why a common rotation makes the risk orientation-independent.

**Dependencies and story role:** M04, M06, M09, M15. It shows that the first budgets can reach the collective benchmark with separate readout.

**Conceptual connection:** The argument uses the spare dimension in which to place the estimate. Qutrits with two specimens are one case of that geometric condition.

**Source pointers:** Anchor §5.3 for averaging, [general onset proof](../science/collective-minimax.md) and [qutrit attainment](../science/finite-budget.md#1-exact-equality-at-two-specimens).

### M17 — A third specimen changes the pair decision

**Central question:** How does a single readout combine with the two parity branches of the pair?

**Understanding target:** Explain the posterior leading-ray decision in the worked receiver. For the antisymmetric branch, use the mean overlap $`1/3`$ and concavity of the optimal conditional score to see why a final unbiased basis is optimal. Track why either order of the two blocks can attain the same risk.

**Dependencies and story role:** M04, M08–M09, M13–M16. It uses the pair mechanism to reach the exact sequential three-specimen score.

**Conceptual connection:** The last block can use the first block's classical outcome. The proof still has to normalize the last measurement on every such history.

**Source pointers:** Anchor §§5.2–5.4 for posterior decisions, [worked receiver](STORY.md#the-third-specimen-changes-the-comparison), [finite pair calculation](../science/finite-budget.md#2-a-three-specimen-attaining-strategy) and [exact sequential optimum](../science/measurement-hierarchy.md).

### M18 — Certifying the entire one-copy comparator

**Central question:** What converts the three-specimen numerical search into a rigorous all-strategy bound?

**Understanding target:** Trace the chain from complete adaptive histories to separable effects, symmetry reduction and a PPT relaxation. Explain why exact rational positivity and dual inequalities certify a fidelity upper bound even though the relaxation's exact optimum is unknown.

**Dependencies and story role:** M06, M08, M11, M17. It supplies the converse matched to the constructed receiver.

**Conceptual connection:** Numerical optimization proposes a certificate; exact verification makes the class-wide inequality usable. Agreement with a few selected one-copy algorithms would not suffice.

**Source pointers:** Anchor §2.4 as optimization context; [PPT converse](../science/finite-budget.md#3-a-certificate-covering-every-adaptive-one-copy-strategy), [exact verifier](../verification/check_finite_budget.py) and [verification scope](../verification/README.md).

### M19 — At the first helpful budget, joint access sets the optimum

**Central question:** Why does the fully antisymmetric sector change the best attainable risk even though this source never populates it?

**Understanding target:** Explain how global normalization forces a POVM to cover the fully antisymmetric sector at $`d`$ specimens. For $`d\ge3`$, relate that coverage to a score penalty for effects with a product decomposition across bipartitions. Order the three-qutrit risks for fully joint readout, biseparable effects, fixed-cut or sequential access, and adaptive one-copy readout. Identify the one-copy row as a lower bound.

**Dependencies and story role:** M11, M15–M18. It joins the exact early tie, the determinant-sector obstruction and the qutrit witnesses into the first ideal synthesis.

**Conceptual connection:** The comparator with effectwise biseparability lets different effects use different cuts. With three qutrits, randomizing complete fixed-cut measurements gives the sequential optimum.

**Source pointers:** Anchor §5.3 for seeded measurements, [first-advantage criterion](../science/collective-minimax.md) and [qutrit comparison](../science/measurement-hierarchy.md).

### M20 — Finite designs and finite random settings

**Central question:** How can a continuous Haar calculation lead to a receiver with finitely many random bits?

**Understanding target:** Explain why a projective design through degree $`N+1`$ preserves collective normalization and pointwise score. For the worked pair apparatus, explain the coupling from its ideal rotation to a finite-bit implementation and include the conditioning fallback in the risk.

**Dependencies and story role:** M05, M09, M19. It connects polynomial moment integration in the ideal optimum to the distinct random-setting problem in the pair implementation.

**Conceptual connection:** The exact collective design integrates finitely many polynomial moments. The practical pair receiver implements its own random rotation approximately and charges the resulting risk.

**Source pointers:** Anchor §5.3 for the covariance principle, [finite collective POVM](../science/collective-minimax.md) and [pair randomization](../science/implementation.md#a-constructive-finite-replacement-for-a-haar-setting).

### M21 — Ancillas and joint operations are resources

**Central question:** What register and controls realize the finite POVMs?

**Understanding target:** Relate the row-isometry construction to a unitary on an input-plus-ancilla register. Count the pair and single readout registers, resets, stored qutrit and complete outcomes; recognize selective joint controls as an explicit assumption.

**Dependencies and story role:** M04–M06, M14, M20. It makes the apparatus concrete enough to audit its resource ledger.

**Conceptual connection:** A finite Naimark realization establishes implementability in a declared control model, while the finite-risk theorem supplies the scientific advantage.

**Source pointers:** Anchor §1.2 for generalized measurements; [explicit finite dilation](../science/implementation.md#explicit-finite-naimark-construction) and [resource ledger](../science/implementation.md#resource-ledger-and-calibration-boundary).

### M22 — Spending the small-budget risk margin

**Central question:** Which implementation errors can be included without losing the strict three-specimen separation?

**Understanding target:** Account for setting approximation, failed conditioning, physical rotation, dilation and output precision in one uniform risk bound. Distinguish a trusted tolerance assumption from calibration data that establish a physical device's tolerance.

**Dependencies and story role:** M19–M21. It joins finite settings and hardware resources to the actual finite comparison.

**Conceptual connection:** A nonzero certified gap supplies an error budget, but numerical compilation alone does not certify physical controls or make their learning free.

**Source pointers:** Anchor §1.2 for risk and §6 for finite-sample limitations; [setting-to-score error](../science/implementation.md#from-setting-error-to-score-error) and [complete implementation guarantee](../science/implementation.md#explicit-finite-naimark-construction).

### M23 — A global matrix estimate from a fixed finite design

**Central question:** How can many pair records be processed without first learning a local coordinate chart?

**Understanding target:** Explain why the 225-ray weighted projective 4-design supplies 450 complete pair outcomes and exact moments for a matrix score. Relate accumulation of that score to a leading-eigenray estimate, rather than a localized likelihood fit.

**Dependencies and story role:** M04, M13–M14, M21. It introduces the separate large-budget construction needed for the noisy and paid-calibration theorem.

**Conceptual connection:** The 450-outcome estimator is a distinct operating point from the 24-outcome small-budget receiver; its Keyl/PSW ingredients are inherited.

**Source pointers:** Anchor §§1.2 and 5.2; [fixed moment receiver](../science/receiver.md#a-fixed-450-outcome-moment-receiver) and [exact noisy moments](../science/memory-noise.md#exact-moments).

### M24 — A finite lower bound for adaptive histories

**Central question:** How does a one-copy information constraint become a global finite-risk lower bound?

**Understanding target:** Connect the per-copy intrinsic information budget, addition of conditional score information and Haar integration by parts. Explain why the resulting finite expression covers biased estimators and all counted pilots without invoking asymptotic attainability.

**Dependencies and story role:** M06–M10, M12. It supplies the larger-budget comparator needed to judge the global matrix receiver.

**Conceptual connection:** Local information is an ingredient in a finite theorem only after the global integration and loss inequalities are supplied.

**Source pointers:** Anchor §§2.1 and 5.5; [global one-copy proof](../science/one-copy-bound.md).

### M25 — Isotropic memory changes a gap, not its ray

**Central question:** Why can the global estimator tolerate unknown depolarizing storage strength without substituting a fitted value?

**Understanding target:** Track the first stored qutrit through the specified channel while the second remains fresh. Explain how the score mean becomes a positive multiple of the target projector plus an identity shift, preserving its leading eigenray.

**Dependencies and story role:** M02, M05, M23. It identifies the precise noise mechanism behind the positive theorem.

**Conceptual connection:** A nuisance that changes an eigenvalue gap differs from an unknown coherent rotation that changes the direction itself.

**Source pointers:** Anchor §2.7 for nuisance-parameter context; [physical memory model](../science/memory-noise.md#physical-memory-model) and [mean and variance](../science/memory-noise.md#exact-moments).

### M26 — Large estimation errors remain in the guarantee

**Central question:** How is the finite matrix estimate controlled when an atypical record produces a bad eigenray?

**Understanding target:** Separate the typical event, controlled by the mean spectral gap, from the concentration failure event assigned bounded loss. Explain how the moment and tail terms form an unconditional risk upper bound without discarding failed localization.

**Dependencies and story role:** M07, M23–M25. It completes the finite-noise comparison before adding a calibration decision.

**Conceptual connection:** The global estimator avoids a localization pilot, but it still pays for rare large errors explicitly. Systematic readout bias also remains in the bound.

**Source pointers:** Anchor §5.5 and §6 as finite-risk context; [finite risk](../science/memory-noise.md#finite-risk-including-large-errors) and [bounded readout errors](../science/memory-noise.md#bounded-additional-readout-errors).

### M27 — A paid reference checks the memory parameter

**Central question:** What can known pure reference pairs learn, and what do they leave assumed?

**Understanding target:** Relate the reference antisymmetric count to storage visibility, and distinguish the good range, indifference band and bad range. Explain why a scalar binomial test does not validate isotropy, independence, reference preparation or every control error.

**Dependencies and story role:** M05, M07, M25–M26. It attaches a concrete calibration experiment to the actual noisy receiver.

**Conceptual connection:** Parameter learning inside a declared model is a narrower task than certifying the entire apparatus model.

**Source pointers:** Anchor §§1.2 and 2.7; [reference experiment](../science/calibration.md#experiment-and-assumptions) and [finite test](../science/calibration.md#exact-finite-calibration-test).

### M28 — Closing the total-budget comparison

**Central question:** Does the advantage remain after references and calibration rejection consume resources and contribute to loss?

**Understanding target:** Combine 200,000 known-reference specimens and 2.8 million signal specimens into the three-million total. Include rejection fallback and bounded readout error, then compare with a one-copy receiver granted all three million as informative signals and ideal apparatus.

**Dependencies and story role:** M05–M07, M24, M26–M27. It closes the large-budget operational loop.

**Conceptual connection:** The good-device risk is unconditional; false acceptance is a separate bad-device soundness statement. Neither postselection nor an uncharged reference supplies the certified gain.

**Source pointers:** Anchor §1.2 for the full experiment's risk; [paid comparison](../science/calibration.md#a-fully-charged-finite-comparison), [readout-error extension](../science/calibration.md#additional-bounded-receiver-errors) and [resource ledger](../science/calibration.md#resource-ledger-and-limits).

### M29 — Two different ways memory can defeat a receiver

**Central question:** Why does the positive depolarizing-memory theorem not imply robustness to arbitrary storage errors?

**Understanding target:** Explain the exchange ambiguity created by an unknown coherent rotation for SWAP-commuting readouts. Separately explain how entanglement-breaking storage can be simulated by one-copy measurement and preparation, ruling out a finite advantage in that channel range.

**Dependencies and story role:** M06, M13, M25, M28. It tests the mechanism at boundaries that change the operational conclusion.

**Conceptual connection:** Identifiability failure and a same-budget classical simulation are distinct obstructions. Their scopes must remain separate from one estimator's sufficient visibility threshold.

**Source pointers:** Anchor §1.2 for identifiability and §6 for model boundaries; [coherent ambiguity](../science/limits.md#an-exchange-ambiguity-for-parity-readouts) and [finite simulation](../science/limits.md#entanglement-breaking-storage-gives-a-finite-simulation).

### M30 — The complete scientific contribution

**Central question:** What can the same missing-ray example establish under ideal collective access and under a calibrated pair receiver's physical constraints?

**Understanding target:** State the exact ideal risk for a uniform occupied hyperplane and the onset at $`d`$ specimens for $`d\ge3`$. Read the four qutrit measurement levels with their precise comparators. Then state the qutrit pair implementation and the separate noisy-memory benefit under the fully charged calibration ledger, including the coherent-error and entanglement-breaking limits.

**Dependencies and story role:** M12–M29. This final synthesis reconnects the ideal theorem and physical operating points to the original task.

**Conceptual connection:** The same ray loss enables a fair specimen comparison while each theorem retains its own source, controls and accounting. The collective construction credits the inherited Keyl measurement. The calibration guarantee measures the gain in specimens under its declared assumptions.

**Source pointers:** Anchor §6 for statistical scope, [collective theorem](../science/collective-minimax.md), [three-qutrit hierarchy](../science/measurement-hierarchy.md), [calibration proof](../science/calibration.md) and [verification scope](../verification/README.md).
