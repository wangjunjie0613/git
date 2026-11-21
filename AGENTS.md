# Research guidance

## Goal
Study open-set weld defect instance localization under complex normal backgrounds. Findings are hypotheses until verified on real data.

## Data and paths
- Resolve the private image/annotation root from `WELD_DATA_ROOT`; no actual server path is published.
- Write private inventories and annotations to `data/private/`; outputs to `runs/`.
- Public repository: do not commit industrial images, reports, client names, private manifests, credentials or trained industrial weights.
- A local inventory does not establish normality, label completeness or access permission.

## Entry points
- `python scripts/inventory.py --root "$WELD_DATA_ROOT" --out data/private/inventory.csv`
- `python scripts/environment_report.py --out runs/environment.json`
- Paper template path: pending user choice in a separate local/private repository. No paper template is included in this public repository.
- Meeting documents, literature tables and paper materials are managed outside this public repository per the user's preference.
- Real image training and inference are NOT_IMPLEMENTED. Do not describe inventory tools as a trained detector.

## Experimental protocol
- Group by physical workpiece/weld before cropping, keeping repeated views together.
- Hold out whole defect families, including directional synonyms, from training and model selection.
- Exclude training images containing held-out defects. Do not reuse historical weights trained on the held-out family.
- Keep incomplete, ambiguous and other-defect annotations under expert review; never silently label them normal.
- Calibrate alert thresholds only on verified complete negative validation images; report realized test FP/image separately.
- Test context must come from an available predictor or metadata. Expert test context is an oracle-only experiment.
- Report candidate coverage, unknown recall, known mAP, false alarms and cluster confidence intervals.
- Test labels are evaluation-only. Synthetic output is never a real experimental result.

## Review
Validate scripts with small fixtures. Compile the actual LaTeX source. Record source and verification scope for references. Do not invent measurements.
