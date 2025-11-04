# Awakening Sleep Nodes: Slack Feature Enhancement (Information Fusion 2025)

[![Paper DOI](https://img.shields.io/badge/DOI-10.1016/S1566--2535(25)00965--0-blue)](https://authors.elsevier.com/sd/article/S1566-2535(25)00965-0)

This is the official implementation for the paper: **"Awakening Sleep Nodes: Slack Feature Enhancement for Robust Long-Term Traffic Forecasting"** (Accepted by Information Fusion).

[cite_start]This work introduces **Slack Feature Enhancement (SFE)**, a simple, plug-and-play, and model-agnostic input-level feature enhancement method[cite: 9]. [cite_start]SFE solves the "sleep node" problem in traffic forecasting, where nodes with low or zero activity provide minimal gradient signals, hindering model performance[cite: 7, 8, 961].

## About This Repository: The `Extralonger+SFE` Example

[cite_start]This repository provides a concrete example of how to integrate SFE into a state-of-the-art baseline, **Extralonger** .

The SFE method is flexible and adapts to the model's architecture.

* **General Case (e.g., STGCN, GWNet):** For models with a `start_conv` layer, integration is as simple as changing the input channels from `C` to `C+1`. The convolutional layer automatically learns to fuse the new SFE feature.

* **This Example (Extralonger):** Extralonger is a "special case" as it uses a direct embedding layer (`t_input`) instead of a `start_conv`. To integrate SFE **without changing any downstream hyperparameters** (like `model_dim`), we use an "embedding split" trick:
    1.  The original `t_input` (outputting 256 dims) is split into two parallel layers.
    2.  `t_input` (outputting 128 dims) processes the main traffic data.
    3.  `tt_input` (outputting 128 dims) processes the SFE feature.
    4.  The two embeddings are concatenated (`128 + 128 = 256`), preserving the `model_dim` for all subsequent attention layers.

This demonstrates how SFE can be seamlessly integrated while respecting the original model's design.

## 🚀 Quick Start: Running the Example

### 1. Environment Setup

We recommend using a Conda environment. The required packages are identical to the baseline model.

```bash
# 1. Clone this repository
git clone [https://github.com/](https://github.com/)[Your-Username]/[Your-Repo-Name].git
cd [Your-Repo-Name]

# 2. (Optional) Create conda env
conda create -n SFE python=3.x
conda activate SFE

# 3. Install requirements
pip install -r requirements.txt
