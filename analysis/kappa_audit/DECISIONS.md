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
