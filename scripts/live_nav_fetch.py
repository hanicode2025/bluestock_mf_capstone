import requests
import pandas as pd
from pathlib import Path

# Folder to save raw data
RAW = Path("data/raw")
RAW.mkdir(parents=True, exist_ok=True)

# Funds to fetch
funds = {
    "SBI_Bluechip":    119598,
    "ICICI_LargeCap":  120586,
    "Nippon_LargeCap": 118632,
    "Axis_LargeCap":   120465,
    "Mirae_LargeCap":  118834,
}


for fund_name, code in funds.items():
    print(f"Fetching {fund_name} ({code})...")
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()

    # Parse NAV history
    df = pd.DataFrame(data["data"])
    df["scheme_code"] = code
    df["scheme_name"] = data["meta"]["scheme_name"]

    # Save to CSV
    filename = RAW / f"{fund_name}_nav.csv"
    df.to_csv(filename, index=False)
    print(f"  Saved {len(df)} rows → {filename}")

print("\nDone! All NAV files saved to data/raw/")