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

# Cleaning functions for each dataset
def clean_orders(df):
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['order_approved_at'] = pd.to_datetime(df['order_approved_at'])
    df['order_delivered_carrier_date'] = pd.to_datetime(df['order_delivered_carrier_date'])
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
    df.drop_duplicates(subset=['order_id'], inplace=True)
    return df

def clean_customers(df):
    df.drop_duplicates(subset=['customer_id'], inplace=True)
    return df

def clean_products(df):
    df.drop_duplicates(subset=['product_id'], inplace=True)
    return df

def clean_order_items(df):
    df.drop_duplicates(subset=['order_id', 'order_item_id'], inplace=True)
    return df

def clean_sellers(df):
    df.drop_duplicates(subset=['seller_id'], inplace=True)
    return df

def clean_payments(df):
    df.drop_duplicates(subset=['order_id', 'payment_sequential'], inplace=True)
    return df

def clean_reviews(df):
    df['review_creation_date'] = pd.to_datetime(df['review_creation_date'])
    df['review_answer_timestamp'] = pd.to_datetime(df['review_answer_timestamp'])
    df.drop_duplicates(subset=['review_id'], inplace=True)
    return df

# Cleaning logic
cleaning_functions = {
    "orders": clean_orders,
    "customers": clean_customers,
    "products": clean_products,
    "order_items": clean_order_items,
    "sellers": clean_sellers,
    "payments": clean_payments,
    "reviews": clean_reviews,
}

# Process each dataset
for file_name, dataset_name in datasets.items():
    file_path = os.path.join(DATA_DIR, file_name)
    print(f"Cleaning {file_name}...")
    df = pd.read_csv(file_path)






































