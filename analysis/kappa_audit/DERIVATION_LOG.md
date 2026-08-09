# Derivation Log — κ Audit

## Entry Template
- **Date:**
- **Contributor:**
- **Step:**
- **Input:**
- **Result:**
- **Evidence:**
  - Equation reference:
  - Notebook:
  - Calculation:
  - Review comment:
- **Verification:**
- **Status:**

---

## Entry 001 — Provisional Diagnostic Reconstruction

**Date:** 2026-08-09

**Contributor:** MOSGM analysis record

**Step:** Provisional observational diagnostic reconstruction and galaxy-level aggregation/bootstrap.

**Input:**
- SPARC raw table1/table2-derived data
- BigQuery diagnostic table: `mosgm_data.v11_1_diagnostic_provisional`
- 175 galaxies
- 3389 radial points in the provisional diagnostic table
- provisional Υ_disk = 0.5
- provisional Υ_bulge = 0.7
- sign-preserving gas term
- Qual/l36/type metadata where available

**Important status:** This is a **Provisional Diagnostic Reconstruction**, not a historical v11.1 reproduction.

**Result:**

Acceleration-binned residual summary:

| x_eff bin | n_points | n_galaxies | mean Δlog g | median Δlog g | RMS |
|---|---:|---:|---:|---:|---:|
| <0.1 | 22 | 13 | -0.152 | -0.255 | 0.393 |
| 0.1-0.2 | 535 | 82 | -0.107 | -0.133 | 0.260 |
| 0.2-0.5 | 1399 | 150 | -0.123 | -0.138 | 0.228 |
| 0.5-1 | 727 | 81 | -0.092 | -0.097 | 0.198 |
| 1-2 | 457 | 55 | -0.037 | -0.054 | 0.169 |
| 2-5 | 227 | 28 | +0.008 | -0.006 | 0.184 |
| >=5 | 22 | 13 | -0.038 | -0.008 | 0.201 |

The provisional reconstruction shows a negative Δlog g signal at low x_eff, with the residual moving toward zero at larger x_eff.

The deepest bin (x_eff < 0.1) has median Δlog g = -0.255. This is numerically close to the proposed asymptotic normalization value log10(κ) ≈ -0.235 for κ = 1/(e−1). This numerical proximity is **not** treated as confirmation of κ.

The x_eff < 0.1 regime contains only 13 galaxies and 22 radial points.

The completed galaxy-level bootstrap analysis for this sparse deep subset gave:
- median = -0.158
- 95% CI = [-0.351, +0.173]
- sign-test p = 0.58

The confidence interval contains both the proposed κ prediction (-0.235) and zero. Therefore the deep-asymptotic κ test is statistically inconclusive.

**Interpretation:**
- A negative residual signal is present in the provisional reconstruction.
- The exact magnitude predicted from κ is not established.
- The sparse x_eff < 0.1 SPARC subset does not have sufficient statistical power to confirm or reject the proposed κ normalization.
- No κ confirmation or rejection is claimed from this reconstruction.

**Limitations:**
1. Υ_disk = 0.5 and Υ_bulge = 0.7 are provisional and were not established here as an exact historical v11.1 reproduction.
2. The reconstruction is diagnostic and provisional, not a reproduction of the historical v11.1 analysis.
3. The principal result documented here is acceleration-binned; no unverified mass-binned conclusion is introduced.
4. The deep-regime sample is sparse and statistically underpowered.
5. This result does not establish causality or model confirmation.
6. Downstream SPARC Pilot/Full analysis must not be started on the basis of this result alone.

**Evidence:**
- BigQuery diagnostic table: `mosgm_data.v11_1_diagnostic_provisional`
- BigQuery acceleration-bin summary
- Galaxy-level aggregation/bootstrap analysis
- Generated CSV artifacts, where preserved separately

**Verification:**
The diagnostic queries and aggregation were executed successfully in BigQuery. Independent reproduction is not claimed unless the corresponding SQL/bootstrap artifacts are separately preserved and rerun.

**Status:** Provisional / Informative / κ unresolved

<!-- Additional entries appended in sequence -->

## Resolution Summary
<!-- Filled only once audit concludes -->
## External Review

**GitHub Discussion:**
- https://github.com/Tarunrbt/MOSGM-Theory/discussions/1

**Purpose:**
- Community mathematical review
- Error reports
- Alternative derivations
- Reviewer feedback

**Audit Policy:**
Only verified mathematical conclusions from the discussion will be recorded in this derivation log. Discussion comments themselves do not constitute accepted results.
