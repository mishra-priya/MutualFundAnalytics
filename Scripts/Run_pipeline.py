"""
Bluestock Mutual Fund Analytics - Master ETL Pipeline

This script performs the main data preparation workflow for the
Bluestock Mutual Fund Analytics project.

Pipeline steps:
1. Load cleaned mutual fund datasets
2. Standardize column names
3. Convert date columns
4. Convert numeric columns
5. Validate AMFI codes
6. Standardize category values
7. Remove duplicate records
8. Handle missing values
9. Calculate NAV returns
10. Save processed pipeline outputs
11. Generate a pipeline summary

Run from the project root:

    python Scripts/Run_pipeline.py
"""

from pathlib import Path
import pandas as pd
import numpy as np


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "Data"

# Existing cleaned datasets
INPUT_DIR = DATA_DIR / "Processed"

# New output directory created by this pipeline
OUTPUT_DIR = DATA_DIR / "Pipeline_Output"

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 2. DATASET FILES
# ============================================================

DATASETS = {
    "fund_master": "clean_fund_master.csv",
    "nav_history": "clean_nav_history.csv",
    "aum_fund_house": "clean_aum_by_fund_house.csv",
    "monthly_sip_inflows": "clean_monthly_sip_inflows.csv",
    "category_inflows": "clean_category_inflows.csv",
    "industry_folio_count": "clean_industry_folio_count.csv",
    "investor_transactions": "clean_investor_transactions.csv",
    "scheme_performance": "clean_scheme_performance.csv",
    "portfolio_holdings": "clean_portfolio_holdings.csv",
    "benchmark_indices": "clean_benchmark_indices.csv",
}


# ============================================================
# 3. STANDARDIZE COLUMN NAMES
# ============================================================

def standardize_columns(df):
    """
    Standardize column names into lowercase snake_case format.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    Returns
    -------
    pandas.DataFrame
        Dataset with standardized column names.
    """

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
        .str.replace("/", "_", regex=False)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
    )

    return df


# ============================================================
# 4. CONVERT DATE COLUMNS
# ============================================================

def convert_dates(df):
    """
    Convert columns containing date-related names into datetime format.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    Returns
    -------
    pandas.DataFrame
        Dataset with converted date columns.
    """

    date_keywords = [
        "date",
        "dob",
        "birth"
    ]

    for column in df.columns:

        if any(
            keyword in column.lower()
            for keyword in date_keywords
        ):

            try:
                df[column] = pd.to_datetime(
                    df[column],
                    errors="coerce"
                )

            except Exception:
                continue

    return df


# ============================================================
# 5. CONVERT NUMERIC COLUMNS
# ============================================================

def convert_numeric_columns(df):
    """
    Convert financial and quantitative columns to numeric data types.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    Returns
    -------
    pandas.DataFrame
        Dataset with numeric columns converted.
    """

    numeric_keywords = [
        "amount",
        "aum",
        "nav",
        "return",
        "alpha",
        "beta",
        "sharpe",
        "sortino",
        "std",
        "risk",
        "drawdown",
        "expense",
        "inflow",
        "folio",
        "count",
        "value",
        "close",
        "price",
        "quantity",
        "weight",
        "profit",
        "sales",
        "age"
    ]

    for column in df.columns:

        if any(
            keyword in column.lower()
            for keyword in numeric_keywords
        ):

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    return df


# ============================================================
# 6. VALIDATE AMFI CODES
# ============================================================

def validate_amfi_codes(df):
    """
    Standardize AMFI code values when the AMFI code column exists.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    Returns
    -------
    pandas.DataFrame
        Dataset with standardized AMFI codes.
    """

    if "amfi_code" in df.columns:

        df["amfi_code"] = (
            df["amfi_code"]
            .astype("string")
            .str.strip()
        )

        invalid_values = [
            "",
            "nan",
            "none",
            "null",
            "na"
        ]

        df.loc[
            df["amfi_code"]
            .str.lower()
            .isin(invalid_values),
            "amfi_code"
        ] = pd.NA

    return df


# ============================================================
# 7. STANDARDIZE CATEGORIES
# ============================================================

def standardize_categories(df):
    """
    Standardize category-related text columns.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    Returns
    -------
    pandas.DataFrame
        Dataset with standardized category values.
    """

    category_columns = [
        column
        for column in df.columns
        if "category" in column.lower()
    ]

    for column in category_columns:

        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
        )

    return df


# ============================================================
# 8. HANDLE MISSING VALUES
# ============================================================

def handle_missing_values(df):
    """
    Handle completely empty rows and columns.

    Text fields are filled with 'Unknown'.

    Numeric missing values are preserved because replacing
    financial values with arbitrary numbers can distort analysis.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    Returns
    -------
    pandas.DataFrame
        Dataset with basic missing-value handling applied.
    """

    # Remove completely empty columns
    df = df.dropna(
        axis=1,
        how="all"
    )

    # Remove completely empty rows
    df = df.dropna(
        axis=0,
        how="all"
    )

    # Fill text columns only
    text_columns = df.select_dtypes(
        include=["object", "string"]
    ).columns

    for column in text_columns:

        df[column] = df[column].fillna(
            "Unknown"
        )

    return df


# ============================================================
# 9. REMOVE DUPLICATES
# ============================================================

def remove_duplicates(df):
    """
    Remove duplicate records from the dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    Returns
    -------
    pandas.DataFrame
        Dataset without duplicate records.
    """

    return (
        df
        .drop_duplicates()
        .reset_index(drop=True)
    )


# ============================================================
# 10. CALCULATE NAV RETURNS
# ============================================================

def calculate_nav_returns(df):
    """
    Calculate percentage NAV returns when the required columns exist.

    Required columns:
    - amfi_code
    - date
    - nav

    Parameters
    ----------
    df : pandas.DataFrame
        NAV history dataset.

    Returns
    -------
    pandas.DataFrame
        NAV dataset with return_pct column.
    """

    required_columns = {
        "amfi_code",
        "date",
        "nav"
    }

    if not required_columns.issubset(
        df.columns
    ):
        return df

    df = df.sort_values(
        ["amfi_code", "date"]
    ).copy()

    df["return_pct"] = (
        df.groupby("amfi_code")["nav"]
        .pct_change()
        .mul(100)
    )

    return df


# ============================================================
# 11. PROCESS ONE DATASET
# ============================================================

def process_dataset(name, filename):
    """
    Load, clean, transform and save one dataset.

    Parameters
    ----------
    name : str
        Logical dataset name.

    filename : str
        CSV filename.

    Returns
    -------
    dict or None
        Dataset processing summary.
    """

    input_path = INPUT_DIR / filename

    # Check whether file exists
    if not input_path.exists():

        print(
            f"WARNING: {filename} not found. Skipping."
        )

        return None

    print(
        f"\nProcessing: {filename}"
    )

    # --------------------------------------------------------
    # Load
    # --------------------------------------------------------

    try:

        df = pd.read_csv(
            input_path,
            low_memory=False
        )

    except Exception as error:

        print(
            f"ERROR: Could not read {filename}"
        )

        print(
            f"Reason: {error}"
        )

        return None

    original_rows = len(df)
    original_columns = len(df.columns)

    # --------------------------------------------------------
    # Transform
    # --------------------------------------------------------

    df = standardize_columns(df)

    df = convert_dates(df)

    df = convert_numeric_columns(df)

    df = validate_amfi_codes(df)

    df = standardize_categories(df)

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    # --------------------------------------------------------
    # NAV return calculation
    # --------------------------------------------------------

    if name == "nav_history":

        df = calculate_nav_returns(df)

    # --------------------------------------------------------
    # Save output
    # --------------------------------------------------------

    output_filename = (
        f"pipeline_{name}.csv"
    )

    output_path = (
        OUTPUT_DIR /
        output_filename
    )

    try:

        df.to_csv(
            output_path,
            index=False
        )

    except Exception as error:

        print(
            f"ERROR: Could not save {output_filename}"
        )

        print(
            f"Reason: {error}"
        )

        return None

    print(
        f"Saved: {output_filename}"
    )

    print(
        f"Rows: {original_rows} -> {len(df)}"
    )

    print(
        f"Columns: {original_columns} -> {len(df.columns)}"
    )

    return {
        "dataset": name,
        "input_file": filename,
        "original_rows": original_rows,
        "final_rows": len(df),
        "original_columns": original_columns,
        "final_columns": len(df.columns)
    }


# ============================================================
# 12. CREATE PIPELINE SUMMARY
# ============================================================

def create_pipeline_summary(results):
    """
    Create a CSV summary of all successfully processed datasets.

    Parameters
    ----------
    results : list
        Dataset processing results.
    """

    if not results:
        return

    summary = pd.DataFrame(
        results
    )

    summary_path = (
        OUTPUT_DIR /
        "pipeline_summary.csv"
    )

    summary.to_csv(
        summary_path,
        index=False
    )

    print(
        "\nPipeline Summary:"
    )

    print(
        summary.to_string(
            index=False
        )
    )

    print(
        f"\nSummary saved to: {summary_path}"
    )


# ============================================================
# 13. MAIN PIPELINE
# ============================================================

def main():
    """
    Execute the complete Bluestock Mutual Fund Analytics pipeline.
    """

    print(
        "\n=============================================="
    )

    print(
        "BLUESTOCK MUTUAL FUND ANALYTICS PIPELINE"
    )

    print(
        "=============================================="
    )

    print(
        f"\nInput folder: {INPUT_DIR}"
    )

    print(
        f"Output folder: {OUTPUT_DIR}\n"
    )

    results = []

    # --------------------------------------------------------
    # Process all datasets
    # --------------------------------------------------------

    for name, filename in DATASETS.items():

        result = process_dataset(
            name,
            filename
        )

        if result is not None:

            results.append(result)

    # --------------------------------------------------------
    # Create summary
    # --------------------------------------------------------

    create_pipeline_summary(
        results
    )

    # --------------------------------------------------------
    # Final status
    # --------------------------------------------------------

    print(
        "\n=============================================="
    )

    if results:

        print(
            "PIPELINE COMPLETED SUCCESSFULLY"
        )

        print(
            f"Datasets processed: {len(results)}"
        )

        print(
            f"Output location: {OUTPUT_DIR}"
        )

    else:

        print(
            "PIPELINE COMPLETED - NO DATASETS PROCESSED"
        )

    print(
        "==============================================\n"
    )


# ============================================================
# 14. SCRIPT ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()