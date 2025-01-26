import pandas as pd
import os

# Define the data directory
DATA_DIR = './data/'
CLEANED_DATA_DIR = './data/cleaned/'

# Ensure the cleaned data directory exists
os.makedirs(CLEANED_DATA_DIR, exist_ok=True)

# Define datasets to clean
datasets = {
    "olist_orders_dataset.csv": "orders",
    "olist_customers_dataset.csv": "customers",
    "olist_products_dataset.csv": "products",
    "olist_order_items_dataset.csv": "order_items",
    "olist_sellers_dataset.csv": "sellers",
    "olist_order_payments_dataset.csv": "payments",
    "olist_order_reviews_dataset.csv": "reviews",
}











































