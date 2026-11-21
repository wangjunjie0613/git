# 开放集焊缝缺陷定位代码仓库

本仓库保留代码、配置示例和研究协作说明。组会课题表、相关工作表、计划和论文材料已从当前版本移除。

## 当前目录

- `AGENTS.md`：研究目标、数据路径约定、代码入口和论文模板位置说明。
- `scripts/inventory.py`：本地文件清点，不上传数据。
- `scripts/environment_report.py`：采集基本Python/GPU环境信息。
- `config/experiment.example.json`：实验配置示例，尚未用于真实训练。
- `.gitignore`：忽略私有数据、结果、权重和本地材料。

## 运行入口

先在本地设置 `WELD_DATA_ROOT` 为实际数据目录，再执行：

```bash
python scripts/inventory.py --root "$WELD_DATA_ROOT" --out data/private/inventory.csv
python scripts/environment_report.py --out runs/environment.json
```

两个脚本仅依赖Python标准库。真实图像训练与推理尚未实现。

## 文档与论文

实验文档和LaTeX材料由用户在本地或单独的私有Git仓库中管理，不放入当前公开仓库。
论文模板路径待用户确定；当前仓库不包含论文模板。
公开仓库禁止提交工业原图、内部报告、私有清单和凭据。
