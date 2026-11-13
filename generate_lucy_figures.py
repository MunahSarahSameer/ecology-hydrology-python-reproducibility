from pathlib import Path
import re
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

root = Path.cwd()
figdir = root / "figures"
datadir = root / "data"
evdir = root / "evidence" / "H05_environment_evidence"
figdir.mkdir(exist_ok=True)

# FIGURE 1: 15-case matrix from recorded evidence
df = pd.read_csv(datadir / "manuscript_ready_15_case_matrix_v2.csv")
df = df.sort_values("candidate_id").reset_index(drop=True)

def yes(v):
    return str(v).strip().upper() in ("YES", "TRUE", "VERIFIED")

attributes = {
    "Baseline passed": df["baseline_status"].eq("PASS"),
    "Later test passed": df["later_test_status"].eq("PASS"),
    "Limited execution": df["later_test_status"].eq("PASS_LIMITED"),
    "Evidence reviewed": df["review_level"].eq("EVIDENCE_REVIEWED"),
    "Checksum match": df["provenance_status"].eq("ZENODO_CHECKSUM_MATCH"),
    "Full workflow verified": df["full_workflow_verified"].map(yes),
    "Published result verified": df["published_results_reproduced"].map(yes)
}
matrix = np.column_stack([v.astype(int) for v in attributes.values()])

fig, ax = plt.subplots(figsize=(13, 7.5))
ax.imshow(matrix, cmap="Greys", vmin=0, vmax=1, aspect="auto")
ax.set_xticks(range(len(attributes)), list(attributes), rotation=35, ha="right")
ax.set_yticks(range(len(df)), df["candidate_id"])
for i in range(len(df)):
    for j in range(len(attributes)):
        ax.text(j, i, "Yes" if matrix[i,j] else "No",
                ha="center", va="center", fontsize=8,
                color="white" if matrix[i,j] else "black")
ax.set_title("Figure 1. Evidence attributes across 15 archived code cases")
ax.set_xlabel("Attributes are scope-specific; a pass does not imply reproduction")
fig.tight_layout()
fig.savefig(figdir / "15_case_attribute_matrix.png", dpi=300)
fig.savefig(figdir / "15_case_attribute_matrix.pdf")
plt.close(fig)

# FIGURE 2: H05 results verified against saved pytest logs
runs = [
    ("h05_recovery", "1.5.3", "3.10.22"),
    ("h05_pandas_203", "2.0.3", "3.10.22"),
    ("h05_pandas_control", "2.3.3", "3.10.22"),
    ("code_decay", "3.1.0", "3.11.18")
]

rows = []
for prefix, pandas_version, python_version in runs:
    log = (evdir / f"{prefix}_pytest_log.txt").read_text(
        encoding="utf-8", errors="replace"
    )
    passed = re.findall(r"(\d+) passed", log)
    failed = re.findall(r"(\d+) failed", log)
    p = int(passed[-1]) if passed else 0
    f = int(failed[-1]) if failed else 0
    if p + f != 3:
        raise ValueError(f"Unexpected H05 test count in {prefix}: {p} passed, {f} failed")
    rows.append({
        "environment": prefix,
        "pandas_version": pandas_version,
        "python_version": python_version,
        "passed": p,
        "failed": f,
        "selected_tests": 3,
        "pytest_log": f"evidence/H05_environment_evidence/{prefix}_pytest_log.txt"
    })

h05 = pd.DataFrame(rows)
h05.to_csv(datadir / "H05_pandas_compatibility_results.csv", index=False)

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(h05))
ax.bar(x, h05["passed"], label="Passed")
ax.bar(x, h05["failed"], bottom=h05["passed"], label="Failed")
ax.set_xticks(x, [
    f"pandas {r.pandas_version}\nPython {r.python_version}"
    for r in h05.itertuples()
])
ax.set_ylim(0, 3.5)
ax.set_ylabel("Selected upstream tests (n=3)")
ax.set_title("Figure 2. H05 selected tests across recorded environments")
ax.legend()
for i, row in enumerate(h05.itertuples()):
    ax.text(i, 3.08, f"{row.passed}/3", ha="center")
fig.text(0.5, 0.01,
         "Final environment also changes Python version; pandas-only causation is not established.",
         ha="center", fontsize=9)
fig.tight_layout(rect=[0, 0.07, 1, 1])
fig.savefig(figdir / "H05_pandas_compatibility.png", dpi=300)
fig.savefig(figdir / "H05_pandas_compatibility.pdf")
plt.close(fig)

readme = """# Lucy feedback — Figure and evidence index

## Figure 1: 15-case evidence matrix
- Figure: `figures/15_case_attribute_matrix.png`
- Source: `data/manuscript_ready_15_case_matrix_v2.csv`
- The matrix records test and verification attributes, not scientific reproduction.

## Figure 2: H05 pandas compatibility
- Figure: `figures/H05_pandas_compatibility.png`
- Source: `data/H05_pandas_compatibility_results.csv`
- Original pytest logs and environment specifications:
  `evidence/H05_environment_evidence/`
- Four environments; three selected upstream tests per environment.
- The final environment also differs in Python version.

## Interpretation
No full published scientific workflow has been independently verified.
Case-level test success must not be interpreted as published-result reproduction.
"""
(root / "FIGURES_AND_EVIDENCE.md").write_text(readme, encoding="utf-8")
print("SUCCESS: Both figures, H05 source CSV and evidence index created.")
