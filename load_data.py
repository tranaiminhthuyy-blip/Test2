import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

def load_data():
    return pd.read_csv(BASE_DIR / "data.csv.gz", compression="gzip")

def load_metadata():
    with open(BASE_DIR / "metadata.json", "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    df = load_data()
    meta = load_metadata()
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")