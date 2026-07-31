-- database: ../Database/bluestock_mf.db



-- ======================================
-- DIMENSION TABLE
-- ======================================

CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT,

    scheme_name TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    launch_date DATE,

    benchmark TEXT,

    expense_ratio_pct REAL,

    exit_load_pct REAL,

    min_sip_amount REAL,

    min_lumpsum_amount REAL,

    fund_manager TEXT,

    risk_category TEXT,

    sebi_category_code TEXT

);


-- ======================================
-- FACT NAV
-- ======================================

CREATE TABLE fact_nav (

    amfi_code INTEGER,

    date DATE,

    nav REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)

);

-- ======================================
-- FACT TRANSACTIONS
-- ======================================

CREATE TABLE fact_transactions (

    investor_id INTEGER,

    transaction_date DATE,

    amfi_code INTEGER,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    city_tier TEXT,

    age_group TEXT,

    gender TEXT,

    annual_income_lakh REAL,

    payment_mode TEXT,

    kyc_status TEXT,


    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)

);


-- ======================================
-- FACT PERFORMANCE
-- ======================================

CREATE TABLE fact_performance (

    amfi_code INTEGER,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    sortino_ratio REAL,

    std_dev_ann_pct REAL,

    max_drawdown_pct REAL,

    aum_crore REAL,

    morningstar_rating INTEGER,

    risk_grade TEXT,


    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)

);

-- ======================================
-- FACT PORTFOLIO
-- ======================================

CREATE TABLE fact_portfolio (

    amfi_code INTEGER,

    stock_symbol TEXT,

    stock_name TEXT,

    sector TEXT,

    weight_pct REAL,

    market_value_cr REAL,

    current_price_inr REAL,

    portfolio_date DATE,


    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)

);


-- ======================================
-- FACT MARKET
-- ======================================

CREATE TABLE fact_market (

    date DATE,

    index_name TEXT,

    close_value REAL

);

-- ======================================
-- FACT SIP INFLOWS
-- ======================================

CREATE TABLE fact_sip_inflows (
    month DATE,
    sip_inflow_crore FLOAT,
    active_sip_accounts_crore FLOAT,
    new_sip_accounts_lakh FLOAT,
    sip_aum_lakh_crore FLOAT,
    yoy_growth_pct FLOAT
);


-- ======================================
-- FACT CATEGORY INFLOWS
-- ======================================

CREATE TABLE fact_category_inflows (
    month DATE,
    category VARCHAR(100),
    net_inflow_crore FLOAT
);


-- ======================================
-- FACT AUM
-- ======================================

CREATE TABLE fact_aum (

    date DATE,

    fund_house TEXT,

    aum_lakh_crore REAL,

    aum_crore REAL,

    num_schemes INTEGER

);


-- ======================================
-- FACT FOLIO COUNT
-- ======================================

CREATE TABLE fact_folio_count (

    month DATE,

    total_folios_crore REAL,

    equity_folios_crore REAL,

    debt_folios_crore REAL,

    hybrid_folios_crore REAL,

    others_folios_crore REAL,

    calculated_total REAL,

    difference REAL

);