# SPARC Mass Models — Raw Input Provenance

## Dataset

- Table: `sparc_mass_models`
- BigQuery: `unified-hull-428117-a4.mosgm_data.sparc_mass_models`
- Source: SPARC Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves
- Reference: Lelli, McGaugh & Schombert (2016)
- Input type: Raw SPARC mass-model radial data

## Load

- Load date: 2026-08-08
- BigQuery ingestion method: Batch CSV load
- Pipeline stage: `raw_input`
- Quality-cut status: Not applied

## Validation

- Total rows: 3391
- Distinct galaxies: 175
- Distinct `(galaxy_id, radius_kpc)` pairs: 3391
- Duplicate `(galaxy_id, radius_kpc)` pairs: 0

## Data-quality checks

- NULL `galaxy_id`: 0
- NULL `distance_mpc`: 0
- NULL `radius_kpc`: 0
- NULL `v_obs_kms`: 0
- NULL `e_vobs_kms`: 0
- NULL `v_gas_kms`: 0
- NULL `v_disk_kms`: 0
- NULL `v_bulge_kms`: 0
- NULL `sb_disk`: 0
- NULL `sb_bulge`: 0
- Invalid distance (`<= 0`): 0
- Invalid radius (`< 0`): 0
- Invalid velocity error (`< 0`): 0

## Population distinction

This table represents the complete raw 175-galaxy input.

The previously reported MOSGM v11.1 validation population of approximately
171 galaxies is a downstream analysis/quality-cut population and must not be
treated as the raw catalog size.

## Governance

This table is a raw input source.

No MOSGM-derived quantities are stored in this table.

Derived quantities, quality-cut populations, predictions, and model outputs
must remain separate from the raw input.
