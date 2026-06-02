import pandas as pd
from pathlib import Path

RAW = Path("data/raw")

# List all CSV files in data/raw
csv_files = list(RAW.glob("*.csv"))

if not csv_files:
    print("No CSV files found in data/raw/")
else:
    for filepath in csv_files:
        print(f"\n{'='*50}")
        print(f"File: {filepath.name}")
        print(f"{'='*50}")
        df = pd.read_csv(filepath)
        print(f"Shape: {df.shape}")
        print(f"\nDtypes:\n{df.dtypes}")
        print(f"\nHead:\n{df.head()}")