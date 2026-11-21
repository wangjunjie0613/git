# 项目说明与开发约定

## 研究目标

研究问题：在不向模型提供留出缺陷类别训练标签或测试示例的条件下，能否在完整焊缝射线原片的复杂正常背景中定位未知缺陷实例，并控制每张原片的误报，同时保持已知类别检测能力？

待检验假设：
1. 固定候选预算下，类别无关候选可能提高小尺寸、低对比未知缺陷的覆盖。
2. 背景条件化正常建模可能优于全局正常原型、简单背景划分和困难负样本基线。
3. 分开进行正常/异常判断与已知/未知拒识，可能改善未知召回与误报之间的权衡。

## 数据路径

通过环境变量 `WELD_DATA_ROOT`指定受控机器上的数据根目录；真实路径只存在于本地环境变量或被忽略的本地配置中。

- `$WELD_DATA_ROOT/raw/`：获授权的完整射线原片。
- `$WELD_DATA_ROOT/annotations/`：专家独立标注、修订和仲裁版本。
- `$WELD_DATA_ROOT/metadata/`：匿名工件、焊缝、原片、视图、设备及来源关联。
- `$WELD_DATA_ROOT/manifests/`：训练、验证、测试和外部测试角色清单。
- `$WELD_DATA_ROOT/reports/`：授权的检测报告及图像关联核对。


## 代码入口及状态

实现顺序和输入输出契约见`scripts/README.md`。计划入口：

1. `validate_manifest.py`：已实现字段和组间泄漏检查。
2. `prepare_data.py`、`make_splits.py)：待实现数据审计、缺陷家族映射和分组划分。
3. `generate_proposals.py`：待实现类别无关候选及候选覆盖评估。
4. `train_detector.py`、`train_normality.py`：待实现闭集、纯异常、全局正常和背景条件基线。
5. `calibrate_threshold.py`：待实现完整阴性验证原片阈值校准。
6. `evaluate_open_set.py`、`bootstrap_ci.py`：待实现一对一定位评估及簇级不确定区间。
7. `summarize_results.py`：待实现表格与可复现报告。

上述待实现脚本目前是带有明确状态标记的入口占位，不得描述为可运行模型。

## 论文模板路径

论文模板保存在仓库`paper/`：

- `paper/main.tex`：中文正文骨架（XeLaTeX）。
- `paper/references.bib`：BibTeX文献库。
- `paper/figures/`：流程图和实验图位置。
- `paper/tables/`：论文表格位置。
- 编译PDF与LaTeX中间文件仅在本地生成，不提交到GitHub。

论文每个章节所需证据见`docs/RESEARCH_MAP.md`。

## 配置与可复现性

- 公开配置模板：`config/experiment.example.json`；本地副本不得提交。
- 每项真实运行记录代码提交哈希、清单版本、配置、随机种子、预训练来源、软件环境和命令。
- 真实结果必须能回溯到冻结的划分和预测文件。合成软件检查不能作为工业检测性能证据。
