import sqlite3
import pandas as pd

conn = sqlite3.connect("../db/ecommerce.db")

queries = {
    "Total Revenue": "SELECT ROUND(SUM(revenue), 2) AS total_revenue FROM ecommerce_data;",
    
    "Monthly Revenue": """
    SELECT order_month, ROUND(SUM(revenue), 2) AS monthly_revenue
    FROM ecommerce_data
    GROUP BY order_month
    ORDER BY order_month;
    """,

    "Top Customers": """
    SELECT customer_unique_id, ROUND(SUM(revenue), 2) AS total_spent
    FROM ecommerce_data
    GROUP BY customer_unique_id
    ORDER BY total_spent DESC
    LIMIT 10;
    """
}

for name, query in queries.items():
    print(f"\n--- {name} ---")
    df = pd.read_sql(query, conn)
    print(df.head())

conn.close()