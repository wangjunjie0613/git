# Code entry points

## Implemented

- `validate_manifest.py`: standard-library CSV check for required columns, unique image IDs, supported split names and specimen/weld leakage.

## Planned, not implemented

1. Image reader and class-agnostic proposal generator with proposal-recall reporting.
2. Frozen-feature baseline for closed-set detection and normal-only anomaly localization.
3. Global-normal and context-conditioned normality methods.
4. Independent unknown rejection and one-to-one IoU evaluation.
5. Clustered confidence intervals and reproducibility reports.

Do not report performance until these components run on audited, authorized real data.
