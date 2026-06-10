import pandas as pd
from pathlib import Path

PROCESSED = Path("data/processed")

def recommend_funds(risk_appetite):
    perf = pd.read_csv(PROCESSED / "07_scheme_performance_clean.csv")
    
    risk_map = {
        'Low': ['Low'],
        'Moderate': ['Moderate', 'Moderately High'],
        'High': ['High', 'Very High']
    }
    
    grades = risk_map.get(risk_appetite, [])
    filtered = perf[perf['risk_grade'].isin(grades)].copy()
    top3 = filtered.nlargest(3, 'sharpe_ratio')[
        ['scheme_name', 'sharpe_ratio', 'return_3yr_pct', 'risk_grade', 'aum_crore']
    ]
    
    print(f"\nTop 3 Fund Recommendations for Risk Appetite: {risk_appetite}")
    print("="*60)
    print(top3.to_string(index=False))

if __name__ == "__main__":
    risk = input("Enter risk appetite (Low / Moderate / High): ")
    recommend_funds(risk)