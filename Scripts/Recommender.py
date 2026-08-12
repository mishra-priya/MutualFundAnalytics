
import pandas as pd
import numpy as np
from pathlib import Path


# ============================================
# CALCULATE SHARPE RATIO
# ============================================

def calculate_sharpe(nav):

    nav["date"] = pd.to_datetime(
        nav["date"],
        errors="coerce"
    )

    nav = nav.sort_values(
        ["amfi_code", "date"]
    )

    nav["daily_return"] = (
        nav.groupby("amfi_code")["nav"]
        .pct_change()
    )

    results = []

    for fund, group in nav.groupby("amfi_code"):

        returns = group["daily_return"].dropna()

        if len(returns) < 30:
            continue

        if returns.std() == 0:
            continue

        sharpe = (
            returns.mean() /
            returns.std()
        ) * np.sqrt(252)

        results.append({
            "amfi_code": fund,
            "Sharpe": sharpe
        })

    return pd.DataFrame(results)


# ============================================
# FUND RECOMMENDER
# ============================================

def recommend_funds(
    nav_file,
    fund_master_file,
    risk_appetite
):

    # Load data
    nav = pd.read_csv(nav_file)
    fund_master = pd.read_csv(fund_master_file)

    # Calculate Sharpe
    sharpe = calculate_sharpe(nav)

    # Merge with fund information
    data = sharpe.merge(
        fund_master[
            [
                "amfi_code",
                "scheme_name",
                "risk_category"
            ]
        ].drop_duplicates("amfi_code"),
        on="amfi_code",
        how="left"
    )

    # Clean risk input
    risk_appetite = (
        risk_appetite
        .strip()
        .title()
    )

    # Validate input
    if risk_appetite not in [
        "Low",
        "Moderate",
        "High"
    ]:

        print(
            "Invalid risk appetite."
        )

        print(
            "Please enter Low, Moderate, or High."
        )

        return None

    # Filter matching risk category
    result = data[
        data["risk_category"]
        .astype(str)
        .str.strip()
        .str.title()
        == risk_appetite
    ]

    # Sort by Sharpe ratio
    result = (
        result
        .sort_values(
            "Sharpe",
            ascending=False
        )
        .head(3)
    )

    return result


# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == "__main__":

    # Project root = folder containing this file
    PROJECT_ROOT = Path(__file__).resolve().parent

    # Correct paths
    NAV_FILE = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "clean_nav_history.csv"
    )

    FUND_MASTER_FILE = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "clean_fund_master.csv"
    )

    # Check files before running
    if not NAV_FILE.exists():

        print(
            f"\nERROR: NAV file not found:\n{NAV_FILE}"
        )

        exit()

    if not FUND_MASTER_FILE.exists():

        print(
            f"\nERROR: Fund master file not found:\n"
            f"{FUND_MASTER_FILE}"
        )

        exit()

    # User input
    risk = input(
        "Enter risk appetite (Low/Moderate/High): "
    )

    # Get recommendations
    result = recommend_funds(
        NAV_FILE,
        FUND_MASTER_FILE,
        risk
    )

    # Display result
    if result is not None:

        print(
            f"\nTop 3 Fund Recommendations "
            f"for {risk.title()} Risk\n"
        )

        if result.empty:

            print(
                "No funds found for this risk category."
            )

        else:

            display_columns = [
                "amfi_code",
                "scheme_name",
                "risk_category",
                "Sharpe"
            ]

            print(
                result[
                    display_columns
                ].to_string(index=False)
            )

