# First data audit

1. Pick one retrievable DR_SD source with physical weld/workpiece IDs. Preserve source ID and raw labels.
2. Export image_id, parent_original_id, workpiece_id, weld_id, view_id, source_id, device_id, batch_id, modality, width, height, bit_depth, annotation_path and report_status into a PRIVATE manifest.
3. Map labels to defect families, weld-location labels, candidate background/indication labels and unresolved labels. Do not decide physical normality from a label name alone.
4. If crack is the held-out family, exclude both longitudinal and transverse crack (and expert-confirmed synonyms). Review other-defect annotations before declaring a training image free of held-out defects.
5. Count independent welds, complete images and instances separately. Handle multiple welds per image with connected grouping: images sharing any weld/workpiece cannot cross splits. Preserve composite-image/subimage relationships.
6. Use expert-reviewed complete normal and difficult-normal images for calibration. Absence of annotation is not evidence of normality. Negative samples must include full originals, not only defect-free patches.
7. Audit legacy train/validation/test manifests and model provenance. Deduplicate copies and repeated views. Keep untouched new batches for final confirmation where possible.
8. Build grouped development and locked-test manifests. Recompute known-only, unknown-only and coexistence for each held-out family.
9. Pilot with a manageable cohort (planning example: 60-100 independent welds, subject to access and class counts), then estimate the full study size using observed uncertainty.
10. Freeze mapping, preprocessing, candidate budgets, thresholds and evaluation rules before final testing. Unknown test labels never select hyperparameters.

## Paths and resource collection
Data root means the top-level folder containing the actual images and/or annotations. Enter that directory and run `pwd`. Set `WELD_DATA_ROOT` to that result locally. Run `nvidia-smi` to record GPU name, card count, available/total memory and driver; separately inspect the selected PyTorch environment. `nvidia-smi`'s CUDA field alone does not establish installed toolkit/PyTorch compatibility.

## Model scope
Start with frozen features and batched tiles. P40 hardware does not imply support for every modern optimized attention or mixed-precision kernel; verify the chosen CUDA/PyTorch build with a small operation before installing an entire training stack. Full training time and memory are measured, not promised.
