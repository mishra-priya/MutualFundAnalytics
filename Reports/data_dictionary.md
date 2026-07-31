# Mutual Fund Analytics - Data Dictionary

## dim_fund

| Column | Data Type | Definition | Source |
|---|---|---|---|
| amfi_code | INTEGER | Unique mutual fund scheme identifier | fund_master.csv |
| fund_house | TEXT | Asset Management Company name | fund_master.csv |
| scheme_name | TEXT | Name of mutual fund scheme | fund_master.csv |
| category | TEXT | Fund category (Equity, Debt, Hybrid etc.) | fund_master.csv |
| sub_category | TEXT | Sub-category of fund | fund_master.csv |
| plan | TEXT | Fund plan type (Direct/Regular) | fund_master.csv |
| launch_date | DATE | Date when scheme was launched | fund_master.csv |
| benchmark | TEXT | Benchmark index used for comparison | fund_master.csv |
| expense_ratio_pct | REAL | Annual expense charged by fund (%) | fund_master.csv |
| exit_load_pct | REAL | Exit load percentage charged on withdrawal | fund_master.csv |
| min_sip_amount | REAL | Minimum SIP investment amount | fund_master.csv |
| min_lumpsum_amount | REAL | Minimum lump sum investment amount | fund_master.csv |
| fund_manager | TEXT | Person managing the fund | fund_master.csv |
| risk_category | TEXT | Risk classification of fund | fund_master.csv |
| sebi_category_code | TEXT | SEBI category identifier | fund_master.csv |



# fact_nav

| Column | Data Type | Definition | Source |
|---|---|---|---|
| amfi_code | INTEGER | Mutual fund scheme identifier | nav_history.csv |
| date | DATE | Date of NAV record | nav_history.csv |
| nav | REAL | Net Asset Value of mutual fund | nav_history.csv |



# fact_transactions

| Column | Data Type | Definition | Source |
|---|---|---|---|
| investor_id | INTEGER | Unique investor identifier | investor_transactions.csv |
| transaction_date | DATE | Date of investment transaction | investor_transactions.csv |
| amfi_code | INTEGER | Mutual fund scheme identifier | investor_transactions.csv |
| transaction_type | TEXT | Type of transaction (SIP/Lumpsum/Redemption) | investor_transactions.csv |
| amount_inr | REAL | Investment amount in Indian Rupees | investor_transactions.csv |
| state | TEXT | Investor state | investor_transactions.csv |
| city | TEXT | Investor city | investor_transactions.csv |
| city_tier | TEXT | City classification | investor_transactions.csv |
| age_group | TEXT | Investor age category | investor_transactions.csv |
| gender | TEXT | Investor gender | investor_transactions.csv |
| annual_income_lakh | REAL | Annual income of investor in lakhs | investor_transactions.csv |
| payment_mode | TEXT | Mode of payment | investor_transactions.csv |
| kyc_status | TEXT | KYC verification status | investor_transactions.csv |



# fact_performance

| Column | Data Type | Definition | Source |
|---|---|---|---|
| amfi_code | INTEGER | Mutual fund scheme identifier | scheme_performance.csv |
| return_1yr_pct | REAL | One year return percentage | scheme_performance.csv |
| return_3yr_pct | REAL | Three year annualized return percentage | scheme_performance.csv |
| return_5yr_pct | REAL | Five year annualized return percentage | scheme_performance.csv |
| benchmark_3yr_pct | REAL | Benchmark return over 3 years | scheme_performance.csv |
| alpha | REAL | Excess return compared to benchmark | scheme_performance.csv |
| beta | REAL | Market sensitivity measure | scheme_performance.csv |
| sharpe_ratio | REAL | Risk-adjusted return measure | scheme_performance.csv |
| sortino_ratio | REAL | Downside risk-adjusted return measure | scheme_performance.csv |
| std_dev_ann_pct | REAL | Annual volatility percentage | scheme_performance.csv |
| max_drawdown_pct | REAL | Maximum fall from peak value | scheme_performance.csv |
| aum_crore | REAL | Assets under management in crore | scheme_performance.csv |
| morningstar_rating | INTEGER | External fund rating | scheme_performance.csv |
| risk_grade | TEXT | Risk category of fund | scheme_performance.csv |



# fact_portfolio

| Column | Data Type | Definition | Source |
|---|---|---|---|
| amfi_code | INTEGER | Mutual fund scheme identifier | portfolio_holdings.csv |
| stock_symbol | TEXT | Stock exchange symbol | portfolio_holdings.csv |
| stock_name | TEXT | Name of stock held by fund | portfolio_holdings.csv |
| sector | TEXT | Industry sector of stock | portfolio_holdings.csv |
| weight_pct | REAL | Percentage weight of stock in portfolio | portfolio_holdings.csv |
| market_value_cr | REAL | Market value of holding in crore | portfolio_holdings.csv |
| current_price_inr | REAL | Current stock price in INR | portfolio_holdings.csv |
| portfolio_date | DATE | Date of portfolio snapshot | portfolio_holdings.csv |



# fact_market

| Column | Data Type | Definition | Source |
|---|---|---|---|
| date | DATE | Market observation date | market_index.csv |
| index_name | TEXT | Name of market index | market_index.csv |
| close_value | REAL | Closing value of market index | market_index.csv |



# fact_sip_inflows

| Column | Data Type | Definition | Source |
|---|---|---|---|
| month | DATE | Month of SIP data | monthly_sip_inflows.csv |
| sip_inflow_crore | REAL | Total SIP inflow amount in crore | monthly_sip_inflows.csv |
| active_sip_accounts_crore | REAL | Active SIP accounts in crore | monthly_sip_inflows.csv |
| new_sip_accounts_lakh | REAL | New SIP registrations in lakh | monthly_sip_inflows.csv |
| sip_aum_lakh_crore | REAL | SIP assets under management in lakh crore | monthly_sip_inflows.csv |
| yoy_growth_pct | REAL | Year-over-year SIP growth percentage | monthly_sip_inflows.csv |



# fact_category_inflows

| Column | Data Type | Definition | Source |
|---|---|---|---|
| month | DATE | Month of category inflow data | category_inflows.csv |
| category | TEXT | Mutual fund category | category_inflows.csv |
| inflow_crore | REAL | Investment inflow amount in crore | category_inflows.csv |
| growth_pct | REAL | Growth percentage of category inflow | category_inflows.csv |



# fact_aum

| Column | Data Type | Definition | Source |
|---|---|---|---|
| date | DATE | AUM measurement date | aum_by_fund_house.csv |
| fund_house | TEXT | Asset Management Company name | aum_by_fund_house.csv |
| aum_lakh_crore | REAL | Total AUM in lakh crore | aum_by_fund_house.csv |
| aum_crore | REAL | Total AUM in crore | aum_by_fund_house.csv |
| num_schemes | INTEGER | Number of schemes managed by fund house | aum_by_fund_house.csv |



# fact_folio_count

| Column | Data Type | Definition | Source |
|---|---|---|---|
| month | DATE | Month of folio statistics | industry_folio_count.csv |
| total_folios_crore | REAL | Total mutual fund folios in crore | industry_folio_count.csv |
| equity_folios_crore | REAL | Equity category folios in crore | industry_folio_count.csv |
| debt_folios_crore | REAL | Debt category folios in crore | industry_folio_count.csv |
| hybrid_folios_crore | REAL | Hybrid category folios in crore | industry_folio_count.csv |
| others_folios_crore | REAL | Other category folios in crore | industry_folio_count.csv |
| calculated_total | REAL | Calculated sum of category folios | industry_folio_count.csv |
| difference | REAL | Difference between reported and calculated total | industry_folio_count.csv |