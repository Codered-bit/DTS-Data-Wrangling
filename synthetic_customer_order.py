# synthetic_dataset_creator.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def create_synthetic_customer_dataset(num_records=1000):
    """
    Create a synthetic customer orders dataset with USA, Nigeria, UK, and UAE
    """
    np.random.seed(42)
    random.seed(42)

    # Define countries with inconsistent formatting as specified
    countries = ["usa", "U.S.A.", "United States", "Nigeria", "NG", "nigeria",
                 "UK", "United Kingdom", "U.K.", "UAE", "Dubai", "dubai"]

    product_categories = ["Electronics", "Clothing", "Books", "Home & Garden",
                         "Sports", "Toys", "Food", "Beauty"]

    customer_names = ["John Smith", "Sarah Johnson", "Mike Brown", "Lisa Wang",
                     "Ahmed Ali", "Maria Garcia", "David Lee", "Emma Wilson"]

    # Generate synthetic data
    data = []
    for i in range(num_records):
        order_id = f"ORD{10000 + i}"
        customer_name = random.choice(customer_names)

        # Generate order date within last 2 years
        days_ago = random.randint(1, 730)
        order_date = datetime.now() - timedelta(days=days_ago)

        product_category = random.choice(product_categories)
        quantity = random.randint(1, 10)
        price = round(random.uniform(10, 500), 2)
        total_amount = quantity * price

        # Intentionally create missing values (10% of records)
        if random.random() < 0.1:
            total_amount = np.nan

        country = random.choice(countries)

        # Create some duplicate rows (5% of records)
        if i > 0 and random.random() < 0.05:
            data.append(data[-1])  # Duplicate previous row
        else:
            data.append({
                "Order ID": order_id,
                "Customer Name": customer_name,
                "Order Date": order_date.strftime("%Y-%m-%d"),
                "Product Category": product_category,
                "Quantity": quantity,
                "Price": price,
                "Total Amount": total_amount,
                "Country": country
            })

    df = pd.DataFrame(data)
    return df

# Create and save the dataset
df = create_synthetic_customer_dataset(1000)
df.to_csv("customer_orders_raw.csv", index=False)
print("Synthetic dataset created: customer_orders_raw.csv")
print(f"Dataset shape: {df.shape}")
print(f"Missing values in Total Amount: {df['Total Amount'].isna().sum()}")
print(f"Duplicate rows: {df.duplicated().sum()}")
print("Country value counts:")
print(df['Country'].value_counts())
