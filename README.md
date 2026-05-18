# Test2

## Overview

This repository contains datasets, supporting documents, and utility scripts for supply chain and logistics analysis.

Large datasets and documents are distributed through GitHub Releases to improve accessibility and compatibility with AI/data-analysis workflows.

---

## Dataset Download

Datasets and supporting resources are available in GitHub Releases:

https://github.com/tranaiminhthuyy-blip/Test2/releases

---

## Available Files

### CSV Datasets
- TransferCost.csv
- STO.csv
- ProductMaster.csv
- LastMileB2BCost.csv
- FirstMileCost.csv
- FacilityMaster.csv
- DailyDemand.csv
- CustomerMaster.csv

### Excel Files
- FC_Investment_Parameters.xlsx
- Data_Dictionary.xlsx
- Case_Answer.xlsx

### Documents
- [SCM26] ĐỀ ROUND 3.pdf

---

## Repository Structure

```text
Test2/
│
├── README.md
├── load_data.py
├── metadata.json
└── datasets.zip (via GitHub Releases)
```

---

## Usage

### 1. Clone repository

```bash
git clone https://github.com/tranaiminhthuyy-blip/Test2.git
```

### 2. Download datasets

Download `datasets.zip` from GitHub Releases.

### 3. Extract files

Extract all CSV files into the same folder as `load_data.py`.

### 4. Run loader

```bash
python load_data.py
```

---

## Notes

- Datasets are stored externally through GitHub Releases.
- Repository is intended for educational, analytics, and research purposes.
- CSV files should remain in the same directory as `load_data.py`.
