# Thirty milestones from a missing ray to a finite receiver

This is the project's common understanding map. Its single educational anchor is Demkowicz-Dobrzański, Górecki and Guţă, *Multi-parameter estimation beyond Quantum Fisher Information*, [arXiv:2001.11742v2](https://arxiv.org/abs/2001.11742v2), published in J. Phys. A **53**, 363001 (2020). The [anchor bridge](ANCHOR.md) translates its estimation language into this project's promised qutrit model.

The map has **12 background/preliminary milestones** and **18 narrative/innovation milestones**. The background connects physical states, measurement records, risk and symmetry into one complete comparison framework. The narrative then builds the pair mechanism and finite converse, makes the receiver implementable, and closes the resource ledger with noise, calibration and limitations. This allocation leaves the specialist algebra in the scientific sources while making the contribution understandable as one story.

Each milestone is a conceptual target, rather than a claim to cover every technical lemma. Dependencies refer to earlier targets; source pointers identify the authoritative statements. Anchor sections supply foundations and context. The qutrit posterior calculations, rational PPT certificate, finite implementation and paid calibration proofs are supplied by this repository and its credited research dependencies, rather than attributed to the review.

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

**Conceptual connection:** The unknown direction is encoded through an absence, while the two occupied directions have no preferred basis inside their plane.

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

**Dependencies and story role:** M04–M05. It fixes the strongest comparator the claimed receiver must beat.

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

**Understanding target:** State the source promise, reported ray, loss, finite specimen ledger, permitted references and measurement classes together. Explain how a constructive upper bound and a full-class lower bound must match these choices.

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

### M15 — Two specimens have a collective ceiling

**Central question:** What limits even an unrestricted joint measurement at total budget two?

**Understanding target:** Follow how a Bayesian reward operator is bounded separately on the symmetric and antisymmetric sectors. Explain why completeness then bounds the fidelity of every collective POVM and every estimator.

**Dependencies and story role:** M08, M11, M13. It establishes a finite obstruction before looking for an advantage.

**Conceptual connection:** A powerful physical pair interaction need not improve the chosen loss at every budget.

**Source pointers:** Anchor §§5.2–5.3; [two-specimen operator bound](../science/finite-budget.md#1-exact-equality-at-two-specimens).

### M16 — Separate measurements attain that ceiling

**Central question:** Why does the two-specimen ceiling prove equality of measurement classes rather than just a lower bound?

**Understanding target:** Explain the one-copy rule that reports a ray perpendicular to both rank-one outcome rays, and how a common twirl supplies a constant-risk implementation. Combine attainability with M15 to obtain the exact risk of 23/40.

**Dependencies and story role:** M09, M14–M15. It completes the first finite-budget comparison.

**Conceptual connection:** Exact equality requires a converse and an attaining strategy under matched assumptions; the absence of a pair benefit at two is an established result, not a failed numerical search.

**Source pointers:** Anchor §5.3, with §5.4 as a separate finite-copy qubit illustration; [two-specimen equality](../science/finite-budget.md#1-exact-equality-at-two-specimens).

### M17 — A third specimen changes the posterior decision

**Central question:** How can one pair record and one separate record produce a useful ray estimate?

**Understanding target:** Interpret the posterior ray matrix for each parity branch and explain why its leading eigenray maximizes conditional mean fidelity. Relate the overlap of the two outcome rays to the branch score.

**Dependencies and story role:** M08, M13–M16. It builds the constructive side of the three-specimen separation.

**Conceptual connection:** The estimator uses both branches and the complete third-specimen outcome; it needs neither a nominal ray nor a localization pilot.

**Source pointers:** Anchor §5.2; [three-specimen strategy](../science/finite-budget.md#2-a-three-specimen-attaining-strategy).

### M18 — Certifying the entire one-copy comparator

**Central question:** What converts the three-specimen numerical search into a rigorous all-strategy bound?

**Understanding target:** Trace the chain from complete adaptive histories to separable effects, symmetry reduction and a PPT relaxation. Explain why exact rational positivity and dual inequalities certify a fidelity upper bound even though the relaxation's exact optimum is unknown.

**Dependencies and story role:** M06, M08, M11, M17. It supplies the converse matched to the constructed receiver.

**Conceptual connection:** Numerical optimization proposes a certificate; exact verification makes the class-wide inequality usable. Agreement with a few selected one-copy algorithms would not suffice.

**Source pointers:** Anchor §2.4 as optimization context; [PPT converse](../science/finite-budget.md#3-a-certificate-covering-every-adaptive-one-copy-strategy), [exact verifier](../verification/check_finite_budget.py) and [verification scope](../verification/README.md).

### M19 — The earliest budget for a pair advantage

**Central question:** What new operational conclusion follows when the two finite comparisons are put together?

**Understanding target:** Combine the exact equality at two with the strict three-specimen upper/lower gap. Distinguish the earliest helpful total budget from an optimal pair receiver or an exact three-specimen one-copy minimax value.

**Dependencies and story role:** M15–M18. This is the first narrative synthesis: the mechanism and converse jointly establish a finite capability.

**Conceptual connection:** A model-specific minimum-budget result survives after the inherited measurement architecture is credited.

**Source pointers:** Anchor §§5.3–5.4 for finite covariant comparison context; [finite statement](../science/finite-budget.md#the-finite-statement) and [attribution](../references/RELATED_WORK.md).

### M20 — Finite randomness preserves the global comparison

**Central question:** How can a continuous Haar calculation lead to a receiver with finitely many random bits?

**Understanding target:** Explain the coupling between an ideal random setting and a finite-bit approximation, including a deterministic fallback for poor conditioning. Recognize why its failure probability contributes to risk rather than causing unlimited retries.

**Dependencies and story role:** M05, M09, M19. It closes a physical interface left open by the ideal covariance argument.

**Conceptual connection:** Finite quantum outcomes and finite random settings are different requirements; both are handled explicitly without assuming an unconstructed exact unitary design.

**Source pointers:** Anchor §5.3 for the ideal covariance principle; [constructive finite randomization](../science/implementation.md#a-constructive-finite-replacement-for-a-haar-setting).

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

**Central question:** What can now be concluded, after inherited methods, assumptions and all relevant costs are stated?

**Understanding target:** Tell the full story: a promised missing ray, no collective benefit at two specimens, a certified finite pair advantage at three, a finite implementation, and a separate noise/calibration theorem with every specimen and failure counted. State the coherent-error boundary and distinguish specimen savings from laboratory-time or hardware-cost claims.

**Dependencies and story role:** M12–M29. This final synthesis reconnects both operating points and their limitations to the original task.

**Conceptual connection:** The contribution is a model-specific finite operational separation and a stated calibration boundary. The architecture, Keyl matrix estimator, general PPT method and earlier two-copy experiments remain credited; neither numerical checks nor a polished receiver certify broader priority or hardware performance.

**Source pointers:** Anchor §6; [scientific route](../science/README.md), [model summary](../science/model.md#results-and-their-domains), [related work](../references/RELATED_WORK.md) and [verification scope](../verification/README.md).
