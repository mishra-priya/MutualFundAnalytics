# Import required libraries.

import pandas as pd            # Used to read, clean, analyze, and modify data
import os                      # Used for handling file paths


# Raw data folder path
folder_path = "data/raw"

# List of all datasets given
datasets = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

# Using loop so that all the process is performed together to all the datasets instead of manual work for each dataset 
for dataset in datasets:
    file_path = os.path.join(folder_path, dataset)
    print("\n" + "=" * 80)
    print("DATASET:", dataset)
    print("=" * 80)


    # Load CSV file
    df = pd.read_csv(file_path)


    # Shape(Shows number of rows and columns)
    print("\nShape:")
    print(df.shape)


    # dtypes(Show datatype of columns)
    print("\nData Types:")
    print(df.dtypes)


    # Head(Show first 5 records)
    print("\nFirst 5 Rows:")
    print(df.head())


    # isnull().sum()(Shows missing values)
    print("\nMissing Values:")
    print(df.isnull().sum())


     # duplicated().sum()(Sum of all duplicate rows in column)
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())


