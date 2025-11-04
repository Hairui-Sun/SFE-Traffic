# Slack Feature Enhancement (SFE) for Traffic Forecasting

[![Paper DOI](https://img.shields.io/badge/DOI-10.1016/S1566--2535(25)00965--0-blue)](https://authors.elsevier.com/sd/article/S1566-2535(25)00965-0)

This is the official implementation for the paper: **"Awakening Sleep Nodes: Slack Feature Enhancement for Robust Long-Term Traffic Forecasting"** (Accepted by Information Fusion).

We introduce **Slack Feature Enhancement (SFE)**, a plug-and-play input-level feature enhancement method to solve the "sleep node" problem in traffic forecasting.

## About This Repository

This repository provides an example of integrating SFE into the **Extralonger** baseline, named `Extralonger+SFE`.

* **General Models (with `start_conv`):** SFE is plug-and-play. Simply change the input channels from `C` to `C+1`.
* **Extralonger (This Example):** This model is a special case. We modify the embedding layer to fuse the SFE feature **without changing any downstream hyperparameters** or the main attention-based architecture.

## 🚀 Quick Start: Running the Example

### 1. Environment Setup

The required packages are identical to the baseline model.

```bash
# 1. Clone this repository
git clone [https://github.com/](https://github.com/)[Your-Username]/[Your-Repo-Name].git
cd [Your-Repo-Name]

# 2. (Optional) Create conda env
conda create -n SFE python=3.x
conda activate SFE

# 3. Install requirements
pip install -r requirements.txt
