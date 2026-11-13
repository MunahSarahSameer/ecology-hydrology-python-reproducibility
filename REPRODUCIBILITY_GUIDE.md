# Research evidence and reproducibility guide

## Study scope

Fifteen worked cases: E01, E02, E03, E06, E07, E08, E10,
H01, H02, H03, H05, H06, H07, H08 and H09.

This is a methods-focused evaluation of archived Python code,
not a claim that all published scientific results were reproduced.

## Source identification

See `provenance/15_case_doi_and_source_register.csv`.

DOIs, source URLs, dates and checksums are transcribed from
the existing research records. A recorded checksum match is
not, by itself, independent verification of an external source.

Consult `provenance/provenance_correction_register.csv`
before relying on H03 or H05 metadata.

E06, E08, E10 and H06 have unresolved authoritative
source identification in the consolidated register.
E10 has a candidate DOI in its source-audit evidence;
it is not independently verified as the tested artifact.

## Evidence locations

- `evidence/case_records/`: 132 sanitised case evidence records
- `evidence/H05_environment_evidence/`: H05 environment
  specifications and selected upstream pytest logs
- `data/manuscript_ready_15_case_matrix_v2.csv`:
  case-level classification data
- `data/H05_pandas_compatibility_results.csv`:
  H05 selected-test results
- `figures/`: manuscript figures

## How to independently inspect a case

1. Find the case in the DOI/source register.
2. Review any correction or unresolved-identity status.
3. Obtain the original code from its authoritative source
   where that source can be established.
4. Compare artifact checksums against the recorded SHA-256
   when the exact archived file is available.
5. Inspect the corresponding case logs for the original
   command, tested component, environment, inputs and output.
6. Recreate the environment only where sufficient package
   and Python-version evidence exists.
7. Compare results with the recorded case-level observations.

Do not treat a successful component test as verification
of a complete scientific workflow.

## Current limitations

- Exact source identity remains unresolved for some cases.
- Complete per-run environment specifications are not
  established for every case.
- Some tests use bounded or modified execution paths.
- Some tests use synthetic or reduced inputs.
- No complete published scientific workflow has been
  independently established as reproduced across the study.
- Sanitised evidence may contain redacted local paths.

No missing commands, dependencies, dates, outputs or
scientific results should be reconstructed by guessing.
