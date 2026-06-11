# Bluestock Mutual Fund Analytics Capstone

A complete mutual fund analytics project built during the Bluestock Fintech Data Analyst Internship (June 2026).

## Project Overview
This project analyses 40 Indian mutual fund schemes across 10 fund houses using real AMFI data. It covers ETL, EDA, performance analytics, advanced risk metrics, and an interactive Tableau dashboard.

## Tech Stack
- Python (Pandas, NumPy, Matplotlib, Seaborn, Plotly, SQLAlchemy)
- SQLite
- Tableau Public
- Google Colab
- GitHub

## Folder Structure

bluestock_mf_capstone/
├── data/raw/           → Original CSV datasets
├── data/processed/     → Cleaned datasets
├── data/db/            → SQLite database
├── notebooks/          → Jupyter notebooks (Days 1-6)
├── scripts/            → Python scripts
├── sql/                → Schema and queries
├── dashboard/          → Tableau dashboard (.twbx)
└── reports/            → Final report, presentation, charts

## Setup Instructions
1. Clone the repo: `git clone https://github.com/hanicode2025/bluestock_mf_capstone`
2. Install dependencies: `pip install -r requirements.txt`
3. Run ETL pipeline: `python scripts/etl_pipeline.py`
4. Open dashboard: Open `dashboard/bluestock_mf_dashboard.twbx` in Tableau

## Dataset Descriptions
| File | Description | Rows |
|------|-------------|------|
| 01_fund_master | Fund metadata, categories, risk grades | 40 |
| 02_nav_history | Daily NAV for all 40 schemes 2022-2026 | 64,320 |
| 03_aum_by_fund_house | Monthly AUM by fund house | 90 |
| 04_monthly_sip_inflows | Monthly SIP inflow data | 48 |
| 05_category_inflows | Net inflows by fund category | 144 |
| 06_industry_folio_count | Industry folio count trends | 21 |
| 07_scheme_performance | Performance metrics per scheme | 40 |
| 08_investor_transactions | Individual investor transactions | 32,778 |
| 09_portfolio_holdings | Stock holdings per fund | 322 |
| 10_benchmark_indices | Nifty 50 and Nifty 100 daily data | 8,050 |

## Key Findings
- Mirae Asset Large Cap has the highest Sharpe Ratio (1.07)
- SBI Small Cap had worst max drawdown (-52.6%) in Oct 2025
- Only 2.2% of SIP investors maintain regular intervals
- ICICI Pru Midcap tops the composite fund scorecard (100/100)

## Internship Details
- Organization: Bluestock Fintech
- Role: Data Analyst Intern
- Duration: May 2026 to July 2026
- Intern: Tadepalli Haneesh