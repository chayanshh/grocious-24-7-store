import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import timedelta # Imported timedelta for date math

# Initializing Faker for generating fake data
fake = Faker()

# Step 2: Define base lists (Changed sets {} to lists [])
# Add as many categories and products as you want
categories = {
    "Furniture"       : ["Office Chair", "Bed", "Sofa", "Bookshelf", "Dining Table"],
    "Electronics"     : ["AC", "Mobiles", "Buds", "Headphones", "Projector"],
    "Office Supplies" : ["Pen", "Sticky Notes", "Notebook", "Stapler", "Ink"],
    "Grocery"         : ["Milk", "Bread", "Eggs", "Fruits", "Vegetables"],
    "Clothing"        : ["T-Shirt", "Jeans", "Jacket", "Sneakers", "Sweater"],
    "Toys"            : ["Action Figure", "Board Game", "Puzzle", "Doll", "RC Car"],
    "Beauty"          : ["Face Wash", "Moisturizer", "Perfume", "Lipstick", "Shampoo"]
}

regions = ["North", "South", "East", "West", "Central", "North-East", "International"]
delivery_statuses = ["Delivered", "Pending", "Cancelled", "Returned"]
payment_modes     = ["Credit Card", "Debit Card", "Net Banking", "UPI", "Cash"]
customer_segments = ["Consumer", "Corporate", "Home Office", "VIP Member", "Small Business", "Wholesale"]

# Step 3: Generate Dataset
records = []  # Empty list to store all rows

for i in range(5000):
    order_id    = f"ORD{1000 + i}"  # Unique order ID
    order_date  = fake.date_between(start_date='-3y', end_date='today') 
    # Fixed timedelta issue here
    ship_date   = order_date + timedelta(days=random.randint(1, 7))

    customer_name    = fake.name()
    customer_id      = f"CUST{random.randint(100, 999)}"
    # Used a new variable name to avoid overwriting the base list
    customer_segment = random.choice(customer_segments)

    category     = random.choice(list(categories.keys()))
    product_name = random.choice(categories[category])
    product_id   = f"PROD{random.randint(1000, 9999)}"

    region = random.choice(regions)
    country = fake.country()
    state  = fake.state()
    city   = fake.city()

    quantity   = random.randint(1, 10)
    unit_price = random.uniform(100, 5000)
    discount   = random.choice([0, 5, 10, 15, 20])

    sales_amount = quantity * unit_price * (1 - discount / 100)
    cost_price   = sales_amount * random.uniform(0.6, 0.9)
    profit       = sales_amount - cost_price

    stock_left = random.randint(0, 50)
    
    if stock_left < 10:
        auto_reorder = "Yes"
        reorder_quantity = random.randint(20, 50) # Fixed typo in variable name
    else:
        auto_reorder = "No"
        reorder_quantity = 0

    supplier_name  = fake.company()
    supplier_email = fake.company_email()
    
    # Used new variable names to avoid overwriting base lists
    payment_mode = random.choice(payment_modes)
    delivery     = random.choice(delivery_statuses)

    # Append row as a dictionary
    records.append({
        "Order ID"            : order_id,
        "Order Date"          : order_date,
        "Ship Date"           : ship_date,
        "Customer Name"       : customer_name,
        "Customer ID"         : customer_id,
        "Customer Segment"    : customer_segment, 
        "Product Name"        : product_name,
        "Category"            : category,
        "Product ID"          : product_id,
        "Region"              : region,
        "Country"             : country,
        "State"               : state,
        "City"                : city,
        "Quantity"            : quantity,
        "Unit Price"          : round(unit_price, 2),
        "Discount (%)"        : discount,
        "Sales Amount"        : round(sales_amount, 2),
        "Cost Price"          : round(cost_price, 2),
        "Profit"              : round(profit, 2),
        "Stock Left"          : stock_left,
        "Auto Reorder"        : auto_reorder,
        "Reorder Quantity"    : reorder_quantity,
        "Supplier Name"       : supplier_name,
        "Supplier Email"      : supplier_email,
        "Payment Mode"        : payment_mode,
        "Delivery Status"     : delivery
    })

# Step 4: Create DataFrame and Save to CSV
df = pd.DataFrame(records)
try:
    df.to_csv("Grocious24_7_data.csv", index=False)
    print("Dataset generated and saved as 'Grocious24_7_data.csv'")
except PermissionError:
    print("Please close the file 'Grocious24_7_data.csv' if it's open in Excel and Power BI.")