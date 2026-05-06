import pandas as pd

def extract_data():
    orders = pd.read_csv("../data/orders.csv")
    order_items = pd.read_csv("../data/order_items.csv")
    customers = pd.read_csv("../data/customers.csv")

    print("Data Loaded Successfully")
    print(f"Orders: {orders.shape}")
    print(f"Order Items: {order_items.shape}")
    print(f"Customers: {customers.shape}")

    return orders, order_items, customers


if __name__ == "__main__":
    extract_data()