# Bluestock Mutual Fund Analytics

## 📊 Mutual Fund Industry Analytics & Performance Dashboard

A complete end-to-end **Mutual Fund Analytics project** developed as part of the Bluestock Data Analytics Capstone. The project analyzes Indian mutual fund industry data using **Python, SQL, PostgreSQL, and Power BI** to understand fund performance, AUM growth, SIP trends, investor behavior, and market trends.

---

## 1. 📌 Project Overview

The mutual fund industry generates large volumes of data across fund schemes, NAVs, assets under management, SIP investments, investor transactions, folio counts, and fund performance.

The objective of this project is to build an end-to-end analytics solution that:

* Collects and validates mutual fund datasets
* Cleans and transforms raw data
* Loads structured data into a relational database
* Performs exploratory and statistical analysis
* Calculates fund performance and risk metrics
* Analyzes investor behavior
* Studies SIP and AUM trends
* Builds an interactive Power BI dashboard
* Provides business insights and recommendations

The project follows a complete **ETL → Database → Analytics → Dashboard → Reporting** workflow.

---

# 2. 🎯 Project Objectives

The major objectives of the project are:

1. **Data Ingestion**

   * Collect and organize mutual fund datasets.
   * Validate input files and required columns.

2. **Data Quality & Cleaning**

   * Handle missing values.
   * Remove duplicate records.
   * Standardize dates and numerical columns.
   * Validate AMFI scheme codes.

3. **Database Design**

   * Design a structured analytical database.
   * Load cleaned datasets into PostgreSQL.
   * Create relationships between fund, NAV, transaction, AUM, SIP, and performance data.

4. **Exploratory Data Analysis**

   * Analyze AUM trends.
   * Study SIP inflows.
   * Analyze investor transactions.
   * Examine folio growth and category-level trends.

5. **Fund Performance Analysis**

   * Analyze returns.
   * Measure volatility and risk.
   * Compare NAV performance against a benchmark.
   * Identify high-performing funds.

6. **Advanced Analytics**

   * Historical Value at Risk (VaR)
   * Conditional Value at Risk (CVaR)
   * Rolling Sharpe Ratio
   * Investor cohort analysis
   * SIP continuity analysis
   * Fund recommendation based on risk appetite
   * Sector concentration using HHI

7. **Dashboard Development**

   * Build an interactive four-page Power BI dashboard.
   * Add filters, tooltips, drill-through, and KPI cards.

8. **Business Recommendations**

   * Convert analytical findings into actionable insights for investors, fund managers, and stakeholders.

---

# 3. 🏗️ Project Architecture

```text
                   RAW DATA
                      │
                      ▼
              Data Ingestion
                      │
                      ▼
             Data Validation
                      │
                      ▼
              Data Cleaning
                      │
                      ▼
              Processed Data
                      │
                      ▼
                PostgreSQL
                      │
            ┌─────────┴─────────┐
            ▼                   ▼
       SQL Analysis       Python Analytics
            │                   │
            └─────────┬─────────┘
                      ▼
               Power BI Dashboard
                      │
             ┌────────┴────────┐
             ▼                 ▼
        Final Report       Presentation
```

---

# 4. 🛠️ Technology Stack

| Technology       | Purpose                     |
| ---------------- | --------------------------- |
| Python           | ETL, cleaning and analytics |
| Pandas           | Data manipulation           |
| NumPy            | Numerical calculations      |
| Matplotlib       | Visualization               |
| Seaborn          | Statistical visualization   |
| SQL              | Data analysis               |
| PostgreSQL       | Relational database         |
| SQLAlchemy       | Python–database connection  |
| psycopg2         | PostgreSQL connectivity     |
| Jupyter Notebook | Exploratory analysis        |
| Power BI         | Interactive dashboard       |
| Git & GitHub     | Version control             |

---

# 5. 📁 Project Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   │   └── Original datasets
│   │
│   └── processed/
│       └── Cleaned datasets
│
├── Scripts/
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── database_loader.py
│   ├── performance_analysis.py
│   ├── investor_analysis.py
│   ├── advanced_analytics.py
│   └── run_pipeline.py
│
├── Notebooks/
│   └── Performance_Analytics.ipynb
│
├── sql/
│   └── queries.sql
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── Dashboard.pdf
│   └── screenshots/
│
├── reports/
│   ├── Final_Report.pdf
│   └── data_dictionary.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 6. 📂 Dataset Description

The project uses multiple datasets covering different aspects of the Indian mutual fund industry.

### 6.1 Fund Master

Contains master information about mutual fund schemes.

Typical fields include:

```text
amfi_code
scheme_name
fund_house
category
sub_category
```

Used for identifying and categorizing mutual fund schemes.

---

### 6.2 NAV History

Contains historical Net Asset Value information.

Typical fields:

```text
amfi_code
date
nav
```

Used for:

* NAV trend analysis
* Return calculation
* Volatility analysis
* Sharpe Ratio
* VaR/CVaR
* Benchmark comparison

---

### 6.3 AUM by Fund House

Contains Assets Under Management information by AMC/fund house.

Used for:

* AMC comparison
* AUM growth analysis
* Market dominance analysis

---

### 6.4 Monthly SIP Inflows

Contains monthly Systematic Investment Plan inflows.

Used for:

* SIP trend analysis
* Monthly growth analysis
* Year-over-year comparison
* Identifying SIP inflow peaks

---

### 6.5 Category Inflows

Contains investment inflows across mutual fund categories.

Used for:

* Category comparison
* Category growth analysis
* Heatmap visualization

---

### 6.6 Industry Folio Count

Contains mutual fund investor folio information.

Used for:

* Investor growth analysis
* Folio trend analysis
* Industry participation analysis

---

### 6.7 Scheme Performance

Contains performance metrics for individual mutual fund schemes.

Used for:

* Fund comparison
* Risk-return analysis
* Fund ranking
* Performance dashboard

---

### 6.8 Investor Transactions

Contains investor-level transaction information.

Used for:

* Transaction analysis
* State-wise investor activity
* SIP/lumpsum/redemption analysis
* Investor behavior analysis
* Cohort analysis

---

# 7. ⚙️ Installation & Setup

## Step 1 — Clone the Repository

```bash
git clone https://github.com/mishra-priya/MutualFundAnalytics.git
```

Move into the project directory:

```bash
cd MutualFundAnalytics
```

---

## Step 2 — Create a Virtual Environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

---

## Step 3 — Install Dependencies

```powershell
pip install -r requirements.txt
```

---

# 8. 🗄️ PostgreSQL Setup

The project uses PostgreSQL as the primary analytical database.

Make sure PostgreSQL is installed and running.

Create the project database:

```sql
CREATE DATABASE bluestock_mf;
```

Configure your database connection in the appropriate Python configuration/script.

Example:

```text
Host: localhost
Port: 5432
Database: bluestock_mf
Username: your_username
Password: your_password
```

> Do not commit database passwords or other credentials to GitHub.

For local development, environment variables can be used.

Example:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bluestock_mf
DB_USER=postgres
DB_PASSWORD=your_password
```

---

# 9. 🚀 Running the ETL Pipeline

The project includes a master execution script:

```text
Scripts/run_pipeline.py
```

Run the complete pipeline using:

```powershell
python Scripts\run_pipeline.py
```

The master pipeline executes the major project stages in sequence:

```text
1. Data ingestion
        ↓
2. Data validation
        ↓
3. Data cleaning
        ↓
4. Database loading
        ↓
5. Performance analytics
        ↓
6. Investor analytics
        ↓
7. Advanced analytics
```

The pipeline is designed to provide a centralized way of executing the project rather than manually running individual scripts.

---

# 10. 📊 Running Individual Analysis Scripts

Individual scripts can also be executed separately when required.

Example:

```powershell
python Scripts\data_ingestion.py
```

```powershell
python Scripts\data_cleaning.py
```

```powershell
python Scripts\database_loader.py
```

```powershell
python Scripts\performance_analysis.py
```

```powershell
python Scripts\investor_analysis.py
```

```powershell
python Scripts\advanced_analytics.py
```

For normal project execution, however, use:

```powershell
python Scripts\run_pipeline.py
```

---

# 11. 📈 SQL Analysis

SQL queries are stored in:

```text
sql/queries.sql
```

Example analytical questions include:

* Top 5 funds by AUM
* Average NAV by month
* SIP inflow YoY growth
* Transactions by state
* Funds with expense ratio below 1%

Example:

```sql
SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;
```

---

# 12. 🧮 Advanced Analytics

The project includes several advanced analytical techniques.

### Historical VaR

Measures the potential loss of a fund at a selected confidence level using historical returns.

### CVaR

Measures the expected loss when returns fall beyond the VaR threshold.

### Rolling Sharpe Ratio

Measures risk-adjusted performance over a rolling time window.

### Investor Cohort Analysis

Groups investors based on characteristics such as investment period or transaction behavior.

### SIP Continuity Analysis

Identifies investors with gaps in SIP activity.

A gap greater than the defined threshold can be flagged for further analysis.

### Fund Recommendation

Funds can be evaluated based on risk-return characteristics and mapped to different investor risk appetites.

### Sector Concentration — HHI

The Herfindahl-Hirschman Index is used to measure portfolio concentration.

---

# 13. 📊 Power BI Dashboard

The Power BI dashboard contains four major pages.

## Page 1 — Industry Overview

Includes:

* Total AUM
* SIP inflows
* Folios
* Number of schemes
* Industry AUM trend
* AUM by AMC

---

## Page 2 — Fund Performance

Includes:

* Fund return vs risk
* Fund scorecard
* NAV trend
* NAV vs benchmark
* Fund-level analysis
* Drill-through functionality

---

## Page 3 — Investor Analytics

Includes:

* Transaction amount by state
* SIP/Lumpsum/Redemption analysis
* Investor age-group analysis
* Monthly transaction volume

---

## Page 4 — SIP & Market Trends

Includes:

* Monthly SIP inflow
* Market benchmark trend
* SIP vs market comparison
* Category-level inflows
* Category trend visualization

---

# 14. 🔎 Dashboard Interactivity

The dashboard supports interactive analysis through:

* Date filters
* Fund filters
* AMC filters
* Category filters
* Tooltips
* Cross-filtering
* Drill-through
* Interactive charts
* KPI cards

The fund-level drill-through allows users to move from the fund performance table to detailed NAV information.

---

# 15. 📌 Key Findings

The analysis identified several important trends in the Indian mutual fund industry.

### AUM Growth

Assets under management showed strong growth during the analysis period, indicating increasing participation and investment in mutual funds.

### AMC Dominance

Large fund houses such as SBI Mutual Fund represented a significant share of industry AUM.

The analysis highlighted SBI's approximately **₹12.5 lakh crore** AUM level by 2025 in the project dataset.

### SIP Growth

Monthly SIP contributions showed a strong upward trend.

The dataset analysis highlighted monthly SIP inflows reaching approximately **₹31,002 crore in December 2025**.

### Folio Growth

Investor folios increased significantly over the analysis period.

The project analysis showed folios increasing from approximately **13.26 crore in January 2022 to 26.12 crore in December 2025**.

### Fund Performance

Risk-return analysis showed that funds with higher returns can also exhibit higher volatility, demonstrating the importance of evaluating risk-adjusted performance rather than returns alone.

---

# 16. 💡 Business Recommendations

Based on the analysis:

### For Investors

* Evaluate both return and risk before selecting a fund.
* Consider investment horizon and risk appetite.
* Compare funds against appropriate benchmarks.
* Maintain SIP continuity for long-term wealth creation.

### For Fund Houses

* Monitor investor retention and SIP continuity.
* Analyze category-level investment trends.
* Identify areas of increasing investor demand.
* Use investor transaction patterns to improve product strategies.

### For Analysts

* Combine NAV, AUM, SIP, transaction, and market data.
* Use risk-adjusted metrics rather than relying only on absolute returns.
* Automate recurring data processing through ETL pipelines.

---

# 17. ⚠️ Limitations

The project has several limitations:

* Data availability may vary across datasets.
* Some datasets may contain aggregated rather than individual-level information.
* Historical data quality depends on the original data source.
* Benchmark selection can influence performance comparisons.
* Risk metrics are dependent on the selected historical period.
* The analysis should not be interpreted as financial advice.
* Dashboard results are based on the datasets included in this project.

---

# 18. 🔮 Future Enhancements

Potential future improvements include:

* Automated daily NAV ingestion
* Real-time AMFI API integration
* Cloud database deployment
* Automated dashboard refresh
* Machine learning-based fund recommendation
* Portfolio optimization
* Sentiment analysis of financial news
* Predictive AUM forecasting
* Investor churn prediction
* Automated email reporting

---

# 19. 📑 Project Deliverables

The final project contains:

| Deliverable                | Status |
| -------------------------- | ------ |
| Data ingestion pipeline    | ✅      |
| Data cleaning & validation | ✅      |
| PostgreSQL database        | ✅      |
| SQL analytical queries     | ✅      |
| Python analytics           | ✅      |
| Advanced analytics         | ✅      |
| Power BI dashboard         | ✅      |
| Dashboard PDF              | ✅      |
| Dashboard screenshots      | ✅      |
| Final report               | ✅      |
| Presentation               | ✅      |
| README                     | ✅      |
| Master ETL pipeline        | ✅      |

---

# 20. 📚 Documentation

Additional documentation is available in:

```text
reports/data_dictionary.md
```

The data dictionary describes the datasets, columns, data types, and business meaning of important fields.

---

# 21. 📊 Dashboard Files

The Power BI dashboard is available at:

```text
dashboard/bluestock_mf_dashboard.pbix
```

The exported dashboard is available at:

```text
dashboard/Dashboard.pdf
```

Dashboard screenshots are available under:

```text
dashboard/screenshots/
```

---

# 22. 🌐 Published Dashboard

If the dashboard is published online, the public/viewer URL can be added here:

```text
Power BI Dashboard:
[Add published dashboard URL here]
```

---

# 23. 👩‍💻 Author

**Priya Mishra**

B.Tech — Data Analytics / Computer Science

Mangalmay Institute of Engineering and Technology

Expected Graduation: 2027

### Technical Skills

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQL
* PostgreSQL
* Power BI
* Excel
* Data Cleaning
* Exploratory Data Analysis
* Statistical Analysis
* Data Visualization

---

# 24. 📜 Project Version

```text
Project: Bluestock Mutual Fund Analytics
Version: v1.0
Status: Final Capstone Submission
Year: 2026
```

---

## ⭐ Conclusion

The Bluestock Mutual Fund Analytics project demonstrates a complete data analytics workflow, beginning with raw financial datasets and progressing through data cleaning, ETL, database management, SQL analysis, Python-based analytics, advanced risk analysis, and interactive Power BI visualization.

The project provides a consolidated analytical view of mutual fund **performance, AUM, SIP investments, investor transactions, folio growth, and market trends**, enabling data-driven interpretation of the mutual fund industry.
