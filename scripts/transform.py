import pandas as pd

def transform_data(orders, order_items, customers):
    # Convert date columns
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

    # Handle missing values
    orders = orders.dropna(subset=['order_purchase_timestamp'])
    order_items = order_items.dropna(subset=['price'])

    # Merge datasets
    df = orders.merge(order_items, on='order_id', how='inner')
    df = df.merge(customers, on='customer_id', how='inner')

    # Feature Engineering
    df['order_date'] = df['order_purchase_timestamp'].dt.date
    df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)

    # Revenue column
    df['revenue'] = df['price'] + df['freight_value']

    df['order_value_category'] = pd.cut(
    df['revenue'],
    bins=[0, 50, 200, 500, 1000, 10000],
    labels=['Low', 'Medium', 'High', 'Very High', 'Premium']
)

    # Basic filtering
    df = df[df['order_status'] == 'delivered']

    print("Transformation Completed")
    print(f"Final dataset shape: {df.shape}")

    return df


if __name__ == "__main__":
    from extract import extract_data

    orders, order_items, customers = extract_data()
    df = transform_data(orders, order_items, customers)

    print(df.head())