# SFE Patch for Extralonger (Information Fusion 2025)

[![Paper DOI](https://img.shields.io/badge/DOI-10.1016/S1566--2535(25)00965--0-blue)](https://authors.elsevier.com/sd/article/S1566-2535(25)00965-0)

This repository provides the patch files to implement the paper: **"Awakening Sleep Nodes: Slack Feature Enhancement for Robust Long-Term Traffic Forecasting"** .

This patch demonstrates how to integrate **Slack Feature Enhancement (SFE)** into the Extralonger baseline.

## 🚀 Installation Guide (File Replacement)

This patch is designed to be applied to the original Extralonger repository.

### Step 1: Clone the Original Extralonger Repo

First, clone the baseline repository:
```bash
git clone [https://github.com/PlanckChang/Extralonger.git](https://github.com/PlanckChang/Extralonger.git)
cd Extralonger
```
### Step 2: Download and Replace Files
Download the following files from this (SFE) repository:

Extralonger_A.py
train_A.py
mask_pems04.npy (and/or other mask files, e.g., mask_pems08.npy)

Now, replace the original files in the Extralonger directory:

```Bash

# (Assuming downloaded files are in ../)
# This replaces the model file:
mv ../Extralonger_A.py ./model.py

# This replaces the training file:
mv ../train_A.py ./train.py
(Note: This assumes the original files are model.py and train.py. Adjust the destination filenames if the originals are named differently, e.g., main.py).
```
### Step 3: Place Mask File
Move the .npy mask files to a directory, for example, ./data/:

```Bash

# (Assuming downloaded files are in ../)
mv ../mask_pems04.npy ./data/
```
Step 3: (CRITICAL) Edit Mask Path
You must manually edit the model file (model.py, which is now your Extralonger_A.py) to point to the correct mask file path.

Open model.py and find this line:

```Python

# mask_path = r"F:\AI_Bulid\Traffic\..."
Change it to the correct relative path:

Python

mask_path = r"data/mask_pems04.npy" 
(Note: Adjust this path if you are using a different dataset, e.g., data/mask_pems08.npy)
```
### Step 5: Run
You can now run the patched training script (train.py, which is now your train_A.py).

```Bash

# Install requirements from the original Extralonger repo first
# pip install -r requirements.txt

# Run the SFE-enabled training
python train.py --model Extralonger --dataset PEMS04 --horizon 48
