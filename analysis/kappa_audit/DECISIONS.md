# Decision Log — κ Audit

## Decision Template
- **Decision ID:**
- **Status:** [Proposed / Accepted / Rejected / Superseded]
- **Reason:**
- **Impact:**
- **Alternatives Considered:**
- **Date:**

---

## Decision 001

- **Decision ID:** K-AUDIT-001
- **Status:** Decision Recorded — Non-Determinative

- **Decision:**
  The provisional diagnostic reconstruction does not establish or reject the proposed κ normalization. The available SPARC deep-regime subset is statistically underpowered for a decisive test of the proposed asymptotic κ value.

- **Reason:**
  - The reconstruction is explicitly provisional and is not a reproduction of the historical v11.1 analysis.
  - The deepest selected regime (x_eff < 0.1) contains only 13 galaxies and 22 radial points.
  - The deepest-bin median Δlog g is approximately -0.255.
  - Galaxy-level bootstrap for this sparse deep subset gives a median Δlog g of approximately -0.158 with a 95% CI of approximately [-0.351, +0.173].
  - The confidence interval contains both the proposed κ prediction (log10 κ ≈ -0.235) and zero.
  - The sign-test result (p ≈ 0.58) is inconclusive.

- **Scope:**
  This decision applies only to the present provisional diagnostic reconstruction. It does not modify the underlying MOSGM theoretical formulation or canonical physical assumptions.

- **Consequence:**
  The reconstruction is retained as an informative diagnostic result, but it is not treated as confirmation or rejection of κ.

- **Analysis Boundary:**
  No SPARC Pilot or SPARC Full analysis shall be initiated on the basis of this reconstruction alone. Further κ resolution requires an independent theoretical derivation and/or an external dataset with substantially greater leverage in the deep regime.

- **Date:** 2026-08-09
- **Source:** DERIVATION_LOG.md, Entry 001
- **Author:** Tarun Kumar Saxena


<!-- Additional decisions appended in sequence -->

## Decision 002

- **Decision ID:** K-AUDIT-002
- **Status:** Proposed — Provenance Gap Identified

- **Decision:**
  The κ bootstrap sensitivity script
  (`analysis/kappa_audit/kappa_bootstrap_sensitivity.py`, introduced in
  commit `b432749`) references an externally defined dataset,
  `diag_stable_18`, described in-code as an "18-galaxy Stable Candidate
  sample." The repository does not preserve a definition, construction
  procedure, membership list, selection criteria, or source artifact for
  `diag_stable_18`. As currently committed, the script is therefore not
  independently executable or reproducible from repository-contained inputs.

- **Reason:**
  - The script references `diag_stable_18` but contains no data-loading,
    query, or import step that defines this object.
  - Direct execution of the committed script produces
    `NameError: name 'diag_stable_18' is not defined`.
  - History searches show that `galaxy_id`, `g_bar`, and `g_obs` first appear
    in the bootstrap script commit `b432749`. The term `x_eff` also appears
    in earlier κ-audit records (`87e9631` and `188176e`), but those records
    do not establish the construction or membership of `diag_stable_18`.
  - Repository filename searches found no file matching `*18*` or
    `*stable*candidate*` outside `.git/`.
  - `data/provenance/sparc_mass_models.md` documents a 171-galaxy downstream
    analysis/quality-cut population, but does not establish that population
    as the source of `diag_stable_18`.
  - `DECISIONS.md` Entry 001 and `DERIVATION_LOG.md` Entry 001 document a
    provisional diagnostic reconstruction involving 175 galaxies, but the
    repository contains no record establishing how, or whether, the
    18-galaxy sample was derived from that population.

- **Impact:**
  The committed bootstrap script cannot currently be executed or validated
  from repository-contained inputs. Consequently, bootstrap results based
  on `diag_stable_18` cannot be treated as independently reproduced from
  the repository until the sample provenance and input data are resolved.

- **Alternatives Considered:**
  - *Reconstruct the 18-galaxy sample from memory or undocumented external
    notes and treat it as the historical sample* — rejected. This would
    conflate a newly reconstructed sample with the historical sample without
    independent verification.
  - *Independently reconstruct a candidate sample from the available source
    data using explicitly documented selection criteria* — proposed as the
    path forward, provided that the reconstruction is clearly identified as
    a new reconstruction and not represented as a historical reproduction.

- **Date:** 2026-08-25
