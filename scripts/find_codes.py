import requests

searches = ['SBI Blue', 'HDFC Top 100', 'ICICI Pru Large', 'Axis Blue', 'Kotak Blue']

for q in searches:
    r = requests.get(f"https://api.mfapi.in/mf/search?q={q}")
    results = r.json()[:4]
    print(f"\n--- {q} ---")
    for s in results:
        print(s['schemeCode'], s['schemeName'])
        