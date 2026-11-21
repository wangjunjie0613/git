# Open-set weld defect localization

Research preparation scaffold. No real-image detection performance has been established.

## Deliverables
- [Research brief](docs/research_brief.md)
- [Eight-paper related-work table](docs/related_work.md) / [CSV](docs/related_work.csv)
- [Seven-day and December milestones](docs/milestones.md)
- [Data audit protocol](docs/data_protocol.md)
- [LaTeX source](paper/main.tex) / [Compiled draft PDF](paper/main.pdf)
- [Agent/research instructions](AGENTS.md)

## Server preparation
```bash
nvidia-smi
pwd
# Replace the placeholder with the real image/annotation directory:
export WELD_DATA_ROOT='/replace/with/actual/data/directory'
python scripts/environment_report.py --out runs/environment.json
python scripts/inventory.py --root "$WELD_DATA_ROOT" --out data/private/inventory.csv
```
The two scripts use only the Python standard library. They do not upload data, train a model, or parse defect annotations. The inventory lists files; it cannot establish weld independence or verify normal images.

## Paper build
Requires XeLaTeX, fontspec, Noto Serif/Sans CJK SC fonts and BibTeX (for example TeX Live plus Noto CJK fonts).
```bash
cd paper
xelatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```
The PDF is a research proposal and paper skeleton: four-part abstract, chapter structure, conceptual placeholder figure and a real bibliography. Results remain pending.

## Status
Public scaffold contains no enterprise source images, client/project statistics, private server paths, or supplied slide deck. Local data availability and GPU details must be checked on the user's server. Industrial reuse of existing trained weights must be audited for held-out-class exposure.
