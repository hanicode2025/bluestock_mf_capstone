-- Bluestock MF Capstone — 10 Analytical Queries

-- Q1. Top 5 funds by AUM
SELECT f.scheme_name, p.aum_crore
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;

-- Q2. Average NAV per month per fund
SELECT amfi_code, strftime('%Y-%m', date) AS month, ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code, month
ORDER BY amfi_code, month;

-- Q3. Transactions by state
SELECT state, COUNT(*) AS total_txns, ROUND(SUM(amount_inr)/1e7, 2) AS total_crore
FROM fact_transactions
GROUP BY state
ORDER BY total_txns DESC;

-- Q4. Funds with expense_ratio < 1%
SELECT scheme_name, fund_house, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;

-- Q5. Top 5 funds by 5yr return
SELECT f.scheme_name, p.return_5yr_pct
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.return_5yr_pct DESC
LIMIT 5;

-- Q6. Transaction count and amount by type
SELECT transaction_type, COUNT(*) AS count,
       ROUND(SUM(amount_inr)/1e7, 2) AS total_crore
FROM fact_transactions
GROUP BY transaction_type
ORDER BY count DESC;

-- Q7. Average Sharpe ratio by category
SELECT f.category, ROUND(AVG(p.sharpe_ratio), 3) AS avg_sharpe
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
GROUP BY f.category;

-- Q8. Top 5 funds by alpha
SELECT f.scheme_name, p.alpha, p.beta, p.sharpe_ratio
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.alpha DESC
LIMIT 5;

-- Q9. Latest AUM by fund house
SELECT fund_house, aum_crore
FROM fact_aum
WHERE date = (SELECT MAX(date) FROM fact_aum)
ORDER BY aum_crore DESC;

-- Q10. Transactions by gender and city tier
SELECT gender, city_tier, COUNT(*) AS count,
       ROUND(AVG(amount_inr), 0) AS avg_amount
FROM fact_transactions
GROUP BY gender, city_tier
ORDER BY gender, city_tier;
