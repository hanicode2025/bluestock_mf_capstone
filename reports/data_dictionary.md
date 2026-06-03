# Data Dictionary — Bluestock MF Capstone

## 1. dim_fund (source: 01_fund_master.csv)
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Primary key. Unique AMFI scheme code assigned by SEBI |
| fund_house | TEXT | Name of the Asset Management Company (AMC) |
| scheme_name | TEXT | Full name of the mutual fund scheme |
| category | TEXT | Broad category — Equity or Debt |
| sub_category | TEXT | SEBI sub-category e.g. Large Cap, Mid Cap, Gilt |
| plan | TEXT | Direct or Regular plan |
| launch_date | DATE | Date the scheme was launched |
| benchmark | TEXT | Index used to benchmark fund performance |
| expense_ratio_pct | REAL | Annual fee charged by AMC as % of AUM (range: 0.1–2.5%) |
| exit_load_pct | REAL | Fee charged on redemption before lock-in period |
| min_sip_amount | INTEGER | Minimum SIP investment amount in INR |
| min_lumpsum_amount | INTEGER | Minimum lump sum investment amount in INR |
| fund_manager | TEXT | Name of the fund manager |
| risk_category | TEXT | SEBI risk grade: Low / Moderate / Moderately High / High / Very High |
| sebi_category_code | TEXT | SEBI internal category code |

## 2. dim_date (derived from fact_nav dates)
| Column | Type | Description |
|--------|------|-------------|
| date | DATE | Primary key. Calendar date |
| year | INTEGER | Calendar year |
| month | INTEGER | Month number (1–12) |
| quarter | INTEGER | Quarter number (1–4) |
| day_of_week | INTEGER | Day of week (0=Monday, 6=Sunday) |
| is_weekend | INTEGER | 1 if Saturday or Sunday, else 0 |

## 3. fact_nav (source: 02_nav_history.csv)
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Foreign key → dim_fund |
| date | DATE | NAV date. Forward-filled for weekends and holidays |
| nav | REAL | Net Asset Value in INR per unit. Must be > 0 |

## 4. fact_transactions (source: 08_investor_transactions.csv)
| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Date of the transaction |
| amfi_code | INTEGER | Foreign key → dim_fund |
| transaction_type | TEXT | Standardised: SIP / Lumpsum / Redemption |
| amount_inr | INTEGER | Transaction amount in INR. Must be > 0 |
| state | TEXT | Indian state of the investor |
| city | TEXT | City of the investor |
| city_tier | TEXT | Tier 1 / Tier 2 / Tier 3 |
| age_group | TEXT | Age bracket of the investor |
| gender | TEXT | Gender of the investor |
| annual_income_lakh | REAL | Annual income in lakhs INR |
| payment_mode | TEXT | Payment method e.g. UPI, Net Banking |
| kyc_status | TEXT | KYC verification status: Verified or Pending |

## 5. fact_performance (source: 07_scheme_performance.csv)
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Foreign key → dim_fund |
| return_1yr_pct | REAL | Trailing 1-year return in % |
| return_3yr_pct | REAL | Trailing 3-year CAGR in % |
| return_5yr_pct | REAL | Trailing 5-year CAGR in % |
| alpha | REAL | Excess return over benchmark |
| beta | REAL | Sensitivity to market movements |
| sharpe_ratio | REAL | Risk-adjusted return (return per unit of risk) |
| sortino_ratio | REAL | Downside risk-adjusted return |
| std_dev_ann_pct | REAL | Annualised standard deviation of returns in % |
| max_drawdown_pct | REAL | Maximum peak-to-trough decline in % |
| aum_crore | INTEGER | Assets Under Management in crore INR |
| morningstar_rating | INTEGER | Morningstar star rating (1–5) |
| risk_grade | TEXT | Internal risk classification |

## 6. fact_aum (source: 03_aum_by_fund_house.csv)
| Column | Type | Description |
|--------|------|-------------|
| date | DATE | Reporting date |
| fund_house | TEXT | Name of the AMC |
| aum_lakh_crore | REAL | Total AUM in lakh crore INR |
| aum_crore | INTEGER | Total AUM in crore INR |
| num_schemes | INTEGER | Number of schemes managed by the fund house |
