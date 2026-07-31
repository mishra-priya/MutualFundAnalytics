-- database: ../Database/bluestock_mf.db

--1. Top 5 funds by AUM

SELECT scheme_name,aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

--2. Average NAV per month

SELECT strftime('%Y-%m', date) AS month,AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

--3. SIP YoY Growth

SELECT month,sip_inflow_crore,yoy_growth_pct
FROM fact_sip_inflows
ORDER BY month;



--4. Number of transactions by state

SELECT state,COUNT(*) AS total_transactions,SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

--5. Low expense ratio funds

SELECT scheme_name,fund_house,expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

--6. Best 5 year performing funds

SELECT scheme_name,return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;


--7. Investment amount by payment mode

SELECT payment_mode,COUNT(*) AS transactions,SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_investment DESC;

--8. Sector exposure of portfolio

SELECT sector,COUNT(*) AS stocks,SUM(weight_pct) AS total_weight
FROM fact_portfolio
GROUP BY sector
ORDER BY total_weight DESC;



--9. Top fund houses by AUM

SELECT fund_house,SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

--10. Risk return comparison

SELECT d.scheme_name,p.return_3yr_pct,p.sharpe_ratio,p.risk_grade
FROM fact_performance p
JOIN dim_fund d
ON p.amfi_code = d.amfi_code
ORDER BY p.sharpe_ratio DESC;
