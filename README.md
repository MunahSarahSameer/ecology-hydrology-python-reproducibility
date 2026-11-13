# Beyond Pass or Fail: Executability and Recovery of Archived Python Research Code in Ecology and Hydrology

## Project overview
This project examines the executability of archived Python research code in ecology and hydrology and documents observed barriers, bounded recovery attempts, and the limits of the resulting evidence.

## Research sample
The working evidence matrix contains 15 cases: 7 ecology and 8 hydrology. Archive ages are recorded only where supported by available provenance evidence.

## Methodology
The study documents archive discovery, baseline assessment, selected code execution, dependency or environment barriers, recovery interventions, and subsequent bounded testing. Execution success is classified according to the scope actually tested.

## Repository structure
- notebooks/: Research setup, archive discovery, and execution/recovery records.
- results/15_case_evidence_matrix.csv: Working classification matrix.
- results/recorded_execution_durations.csv: Durations explicitly recorded in JSON evidence.
- evidence/main_results/: JSON evidence copied from the main results directory.
- evidence/repository_results/: JSON evidence copied from repository-level results.

## Current findings
The working matrix contains 13 PASS_LIMITED and 2 PASS later-test classifications. These classifications refer to selected tested scopes, not complete scientific workflows. No case is recorded as having a verified full workflow or verified reproduction of published results.

## Execution duration
Five JSON evidence files contain explicit duration fields. Recorded durations are not directly comparable across different test scopes and must not be interpreted as measured human recovery effort.

## Reproducibility and limitations
The publication notebooks and JSON evidence have been sanitised to remove detected personal email addresses and local username references. Absolute local paths may require reconfiguration before rerunning. Some tests use synthetic inputs, modified recovery runners, or selected components. Successful bounded execution does not establish reproduction of published scientific findings. Archive age alone does not establish the cause of a failure.

## Evidence integrity
Original research files and separate backups are retained outside this publication folder. The repository presents selected evidence and a working research classification, rather than a verified reproduction of all published results.
