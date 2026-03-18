# EasyProDock

[中文](#中文) | [English](#english)

---

## English

### 🧬 Protein Structure Prediction & Molecular Docking Software

EasyProDock is an all-in-one desktop application for protein structure prediction and molecular docking, featuring a full Chinese interface and offline operation capability.

### ✨ Features

- **Protein Structure Prediction**: Support single/double chain amino acid sequences (≤800 residues) with high-precision tertiary structure prediction in 5-12 minutes
- **Binding Pocket Recognition**: Automatic identification of protein binding pockets using P2Rank with rainbow color highlighting
- **Drug Molecule Library**: Built-in library of 50 common drug molecules with support for custom ligand upload (SDF/MOL2 format)
- **High-throughput Molecular Docking**: One-click molecular docking using AutoDock Vina with smina re-scoring, outputting Top10 conformations
- **3D Visualization**: Interactive py3Dmol visualization with rotation, zoom, and style switching
- **PDF Report Generation**: One-click generation of experiment reports with university watermark

### 🛠️ Tech Stack

- **Language**: Python 3.8+
- **GUI Framework**: PySide6
- **Core Algorithms**: AlphaFold, P2Rank, AutoDock Vina, smina
- **Visualization**: py3Dmol
- **Packaging**: PyInstaller

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/dsadsasdaddas/easydock-protein.git
cd easydock-protein

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m easyprodock
```

### 🚀 Quick Start

1. Input protein amino acid sequence (single or double chain, max 800 residues)
2. Click "Predict Structure" to generate tertiary structure
3. Select binding pockets from the automatically identified options
4. Choose ligands from built-in library or upload custom molecules
5. Run molecular docking and view Top10 conformations
6. Export results as PDF report

### 📋 Requirements

- Python 3.8+
- Windows 10/11 or macOS 10.14+
- RAM: 8GB minimum, 16GB recommended
- GPU: Optional, for faster structure prediction

### 📄 License

MIT License

---

## 中文

### 🧬 蛋白质结构预测与分子对接一体化软件

EasyProDock 是一款全中文、纯本地运行、可单文件分发的蛋白质结构预测与分子对接一体化桌面软件。

### ✨ 功能特性

- **蛋白质结构预测**：支持单链或双链蛋白氨基酸序列（≤800残基），5-12分钟内输出高精度三级结构
- **结合口袋识别**：基于 P2Rank 自动识别蛋白质结合口袋，彩虹色高亮显示
- **药物分子库**：内置50种常见药物分子，支持用户上传自定义配体（SDF/MOL2格式）
- **高通量分子对接**：一键进行分子对接，结合 AutoDock Vina 和 smina 重打分，输出Top10构象
- **3D可视化**：py3Dmol 交互式3D可视化，支持旋转、缩放、样式切换
- **PDF报告生成**：一键生成带学校水印的实验报告

### 🛠️ 技术栈

- **开发语言**：Python 3.8+
- **界面框架**：PySide6
- **核心算法**：AlphaFold、P2Rank、AutoDock Vina、smina
- **可视化**：py3Dmol
- **打包工具**：PyInstaller

### 📦 安装

```bash
# 克隆仓库
git clone https://github.com/dsadsasdaddas/easydock-protein.git
cd easydock-protein

# 安装依赖
pip install -r requirements.txt

# 运行程序
python -m easyprodock
```

### 🚀 快速开始

1. 输入蛋白质氨基酸序列（单链或双链，最大800残基）
2. 点击"预测结构"生成三级结构
3. 从自动识别的结合口袋中选择目标口袋
4. 从内置分子库选择配体或上传自定义分子
5. 运行分子对接，查看Top10构象
6. 导出PDF报告

### 📋 系统要求

- Python 3.8+
- Windows 10/11 或 macOS 10.14+
- 内存：最低8GB，推荐16GB
- GPU：可选，用于加速结构预测

### 📄 许可证

MIT License

---

## 👥 Authors

EasyProDock Team

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.