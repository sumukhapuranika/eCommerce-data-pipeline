import sqlite3
from transform import transform_data
from extract import extract_data

def load_to_db(df):
    conn = sqlite3.connect("../db/ecommerce.db")

    # Save table
    df.to_sql("ecommerce_data", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print("Data loaded into SQLite database successfully")



if __name__ == "__main__":
    orders, order_items, customers = extract_data()
    df = transform_data(orders, order_items, customers)

    load_to_db(df)