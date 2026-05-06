# E-commerce Data Pipeline & Analysis

## 📌 Overview
Built an end-to-end data pipeline to extract, transform, and analyze e-commerce data using Python and SQL.

## ⚙️ Tech Stack
- Python (Pandas)
- SQL (SQLite)
- Data Visualization (Matplotlib, Seaborn)

## 🔄 Pipeline
- Extract: Loaded raw CSV data
- Transform: Cleaned and merged datasets, created features like revenue and order categories
- Load: Stored processed data into SQLite database
- Analyze: Queried data using SQL and generated insights

## 📊 Key Insights
- Revenue shows consistent monthly trends
- Top customers contribute a significant portion of total revenue
- Certain cities dominate order volume

## 🚀 How to Run
1. Run extract.py
2. Run transform.py
3. Run load.py
4. Run run_queries.py
5. Open analysis.ipynb

## 📁 Project Structure
ecommerce-data-pipeline/
│
├── data/
│   ├── orders.csv
│   ├── order_items.csv
│   └── customers.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│
├── db/
│   └── ecommerce.db
│
├── analysis/
│   └── analysis.ipynb
│
├── queries.sql
└── README.md