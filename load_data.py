from sqlalchemy import create_engine
import pandas as pd


# SQLite database connection
engine = create_engine(
    "sqlite:///database/bluestock_mf.db"
)


# Load cleaned CSV files

dim_fund = pd.read_csv(
    "data/processed/clean_fund_master.csv"
)

fact_nav = pd.read_csv(
    "data/processed/clean_nav_history.csv"
)

fact_transactions = pd.read_csv(
    "data/processed/clean_investor_transactions.csv"
)

fact_performance = pd.read_csv(
    "data/processed/clean_scheme_performance.csv"
)

fact_portfolio = pd.read_csv(
    "data/processed/clean_portfolio_holdings.csv"
)

fact_market = pd.read_csv(
    "data/processed/clean_market_index.csv"
)

fact_sip_inflows = pd.read_csv(
    "data/processed/clean_monthly_sip_inflows.csv"
)

fact_category_inflows = pd.read_csv(
    "data/processed/clean_category_inflows.csv"
)

fact_aum = pd.read_csv(
    "data/processed/clean_aum_by_fund_house.csv"
)

fact_folio_count = pd.read_csv(
    "data/processed/clean_industry_folio_count.csv"
)
# Load DataFrames into SQLite

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="append",
    index=False
)


fact_nav.to_sql(
    "fact_nav",
    engine,
    if_exists="append",
    index=False
)


fact_transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="append",
    index=False
)


fact_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="append",
    index=False
)


fact_portfolio.to_sql(
    "fact_portfolio",
    engine,
    if_exists="append",
    index=False
)


fact_market.to_sql(
    "fact_market",
    engine,
    if_exists="append",
    index=False
)


fact_sip_inflows.to_sql(
    "fact_sip_inflows",
    engine,
    if_exists="append",
    index=False
)


fact_category_inflows.to_sql(
    "fact_category_inflows",
    engine,
    if_exists="append",
    index=False
)


fact_aum.to_sql(
    "fact_aum",
    engine,
    if_exists="append",
    index=False
)


fact_folio_count.to_sql(
    "fact_folio_count",
    engine,
    if_exists="append",
    index=False
)


print("All cleaned datasets loaded successfully into SQLite!")


from sqlalchemy import text


tables=[
"dim_fund",
"fact_nav",
"fact_transactions",
"fact_performance",
"fact_aum"
]


with engine.connect() as con:

    for table in tables:

        result=con.execute(
            text(
            f"SELECT COUNT(*) FROM {table}"
            )
        )

        print(
            table,
            result.scalar()
        )



