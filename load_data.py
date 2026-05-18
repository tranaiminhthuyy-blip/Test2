import pandas as pd
from pathlib import Path

# =========================================================
# Configuration
# =========================================================

DATA_FOLDER = Path(".")

CSV_FILES = {
    "TransferCost": "TransferCost.csv",
    "STO": "STO.csv",
    "ProductMaster": "ProductMaster.csv",
    "LastMileB2BCost": "LastMileB2BCost.csv",
    "FirstMileCost": "FirstMileCost.csv",
    "FacilityMaster": "FacilityMaster.csv",
    "DailyDemand": "DailyDemand.csv",
    "CustomerMaster": "CustomerMaster.csv",
}

# =========================================================
# Load datasets
# =========================================================

datasets = {}

print("=" * 60)
print("LOADING DATASETS")
print("=" * 60)

for dataset_name, file_name in CSV_FILES.items():

    file_path = DATA_FOLDER / file_name

    try:
        df = pd.read_csv(file_path)

        datasets[dataset_name] = df

        print(f"\n[SUCCESS] {dataset_name}")
        print(f"File: {file_name}")
        print(f"Shape: {df.shape}")

        print("\nColumns:")
        print(list(df.columns))

        print("\nPreview:")
        print(df.head(3))

        print("-" * 60)

    except FileNotFoundError:
        print(f"\n[ERROR] File not found: {file_name}")

    except Exception as e:
        print(f"\n[ERROR] Failed to load {file_name}")
        print(f"Reason: {e}")

# =========================================================
# Summary
# =========================================================

print("\n")
print("=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

for name, df in datasets.items():
    print(f"{name}: {df.shape[0]} rows x {df.shape[1]} columns")

print("\nAll available datasets loaded successfully.")
