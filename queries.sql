-- 1. Total Revenue
SELECT ROUND(SUM(revenue), 2) AS total_revenue
FROM ecommerce_data;

-- 2. Monthly Revenue Trend
SELECT order_month, ROUND(SUM(revenue), 2) AS monthly_revenue
FROM ecommerce_data
GROUP BY order_month
ORDER BY order_month;

-- 3. Top 10 Customers by Revenue
SELECT customer_unique_id, ROUND(SUM(revenue), 2) AS total_spent
FROM ecommerce_data
GROUP BY customer_unique_id
ORDER BY total_spent DESC
LIMIT 10;

-- 4. Order Count by Status
SELECT order_status, COUNT(*) AS total_orders
FROM ecommerce_data
GROUP BY order_status;

-- 5. Revenue by Order Value Category
SELECT order_value_category, ROUND(SUM(revenue), 2) AS revenue
FROM ecommerce_data
GROUP BY order_value_category
ORDER BY revenue DESC;

-- 6. Top 10 Cities by Orders
SELECT customer_city, COUNT(*) AS total_orders
FROM ecommerce_data
GROUP BY customer_city
ORDER BY total_orders DESC
LIMIT 10;