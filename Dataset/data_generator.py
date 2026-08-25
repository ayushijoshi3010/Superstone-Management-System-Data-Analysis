# Importing all the required libraries

import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import date


# Initializing Faker for collecting fake data

fake = Faker('en_IN')


# ---------------------------------------------------------
# DEFINING BASE LISTS
# ---------------------------------------------------------

categories = {
    "Furniture": [
        "Office Chairs",
        "Study Table",
        "Sofa",
        "Bookshelf",
        "Dining Table"
    ],

    "Office Supplies": [
        "Pen",
        "Notebook",
        "Stapler",
        "File Folder",
        "Calculator"
    ],

    "Electronics": [
        "Laptop",
        "Keyboard",
        "Mouse",
        "Headphones",
        "Monitor"
    ],

    "Grocery": [
        "Rice Bag",
        "Cooking Oil"
    ]
}


regions = [
    "North",
    "South",
    "East",
    "West"
]


payment_modes = [
    "Cash",
    "Credit Card",
    "UPI",
    "Net Banking"
]


delivery_status = [
    "Delivered",
    "Pending",
    "Returned",
    "Cancelled"
]


customer_segments = [
    "Consumer",
    "Corporate",
    "Home Office"
]


# ---------------------------------------------------------
# CUSTOMER MASTER DATA
# ---------------------------------------------------------

customers = {}

while len(customers) < 300:

    customer_name = fake.name()

    if customer_name not in customers:

        customers[customer_name] = {

            "Customer Id":
                f"CUST{1000 + len(customers)}",

            "Customer Segment":
                random.choice(customer_segments),

            "State":
                fake.state(),

            "City":
                fake.city()
        }


# ---------------------------------------------------------
# SUPPLIER MASTER DATA
# ---------------------------------------------------------

suppliers = {}

category_names = list(categories.keys())


while len(suppliers) < 25:

    supplier_name = fake.company()

    if supplier_name not in suppliers:

        category = category_names[
            len(suppliers) % len(category_names)
        ]

        suppliers[supplier_name] = {

            "Supplier Email":
                fake.company_email(),

            "Category":
                category
        }


# List of all 25 suppliers

supplier_names = list(suppliers.keys())


# ---------------------------------------------------------
# PRODUCTS THAT NEED REORDER
# ---------------------------------------------------------

reorder_products = [

    "Stapler",

    "Laptop",

    "Cooking Oil",

    "Office Chairs",

    "Rice Bag"
]


# ---------------------------------------------------------
# PRODUCT MASTER DATA
# ---------------------------------------------------------

products = {}


for category, product_list in categories.items():

    for product in product_list:

        # Generate unit price

        unit_price = random.randint(
            100,
            15000
        )


        # Generate cost price

        cost_price = round(
            unit_price * random.uniform(
                0.3,
                0.8
            ),
            2
        )


        # -------------------------------------------------
        # INVENTORY INFORMATION
        # -------------------------------------------------

        if product in reorder_products:

            # Low stock products

            stock_left = random.randint(
                5,
                20
            )

            reorder_point = random.randint(
                25,
                35
            )

            auto_reorder = "Yes"

            reorder_quantity = random.randint(
                30,
                60
            )

        else:

            # Healthy stock products

            stock_left = random.randint(
                40,
                100
            )

            reorder_point = random.randint(
                15,
                30
            )

            auto_reorder = "No"

            reorder_quantity = 0


        # -------------------------------------------------
        # STORE PRODUCT INFORMATION
        # -------------------------------------------------

        products[product] = {

            "Product Id":
                f"PROD{1000 + len(products)}",

            "Category":
                category,

            "Unit Price":
                unit_price,

            "Cost Price":
                cost_price,

            "Stock Left":
                stock_left,

            "Reorder Point":
                reorder_point,

            "Auto Reorder":
                auto_reorder,

            "Reorder Quantity":
                reorder_quantity
        }


# ---------------------------------------------------------
# GENERATE FAKE ORDER DATA
# ---------------------------------------------------------

records = []


for i in range(1000):

    # -----------------------------------------------------
    # ORDER INFORMATION
    # -----------------------------------------------------

    order_id = f"ORD{1000 + i}"


    

    order_date = fake.date_between(
    start_date=date(2023, 1, 1),
    end_date=date(2025, 12, 31)
)

    ship_date = (
    order_date
    + pd.Timedelta(days=random.randint(1, 7))
)


    # -----------------------------------------------------
    # CUSTOMER INFORMATION
    # -----------------------------------------------------

    customer_name = random.choice(
        list(customers.keys())
    )


    customer_id = customers[
        customer_name
    ]["Customer Id"]


    customer_segment = customers[
        customer_name
    ]["Customer Segment"]


    state = customers[
        customer_name
    ]["State"]


    city = customers[
        customer_name
    ]["City"]


    # -----------------------------------------------------
    # SUPPLIER AND PRODUCT SELECTION
    # -----------------------------------------------------

    # For the first 25 orders, use each supplier once.
    # This guarantees that all 25 suppliers appear
    # in the final dataset.

    if i < 25:

        supplier_name = supplier_names[i]

        supplier_category = suppliers[
            supplier_name
        ]["Category"]

        category = supplier_category

    else:

        # Random category for remaining orders

        category = random.choice(
            list(categories.keys())
        )

        # Select a supplier belonging to that category

        available_suppliers = [

            supplier

            for supplier, details
            in suppliers.items()

            if details["Category"] == category
        ]

        supplier_name = random.choice(
            available_suppliers
        )


    supplier_email = suppliers[
        supplier_name
    ]["Supplier Email"]


    # -----------------------------------------------------
    # PRODUCT INFORMATION
    # -----------------------------------------------------

    product_name = random.choice(
        categories[category]
    )


    product_id = products[
        product_name
    ]["Product Id"]


    unit_price = products[
        product_name
    ]["Unit Price"]


    cost_price = products[
        product_name
    ]["Cost Price"]


    # -----------------------------------------------------
    # INVENTORY INFORMATION
    # -----------------------------------------------------

    stock_left = products[
        product_name
    ]["Stock Left"]


    reorder_point = products[
        product_name
    ]["Reorder Point"]


    auto_reorder = products[
        product_name
    ]["Auto Reorder"]


    reorder_quantity = products[
        product_name
    ]["Reorder Quantity"]


    # -----------------------------------------------------
    # SALES INFORMATION
    # -----------------------------------------------------

    region = random.choice(
        regions
    )


    quantity = random.randint(
        1,
        10
    )


    discount = random.choice(
        [0, 5, 10, 15, 20]
    )


    sales_amount = (
        unit_price
        * quantity
        * (1 - discount / 100)
    )


    # -----------------------------------------------------
    # COST AND PROFIT
    # -----------------------------------------------------

    total_cost = (
        cost_price
        * quantity
    )


    profit = (
        sales_amount
        - total_cost
    )


    # -----------------------------------------------------
    # PAYMENT AND DELIVERY
    # -----------------------------------------------------

    payment_mode = random.choice(
        payment_modes
    )


    delivery = random.choice(
        delivery_status
    )


    # -----------------------------------------------------
    # APPEND ROW
    # -----------------------------------------------------

    records.append({

        "Order Id":
            order_id,

        "Order Date":
            order_date.strftime(
                '%d-%m-%Y'
            ),

        "Ship Date":
            ship_date.strftime(
                '%d-%m-%Y'
            ),

        "Customer Id":
            customer_id,

        "Customer Name":
            customer_name,

        "Customer Segment":
            customer_segment,

        "Product Id":
            product_id,

        "Product Name":
            product_name,

        "Category":
            category,

        "Region":
            region,

        "State":
            state,

        "City":
            city,

        "Quantity":
            quantity,

        "Unit Price":
            unit_price,

        "Discount %":
            discount,

        "Sales Amount":
            round(
                sales_amount,
                2
            ),

        "Cost Price":
            round(
                cost_price,
                2
            ),

        "Profit":
            round(
                profit,
                2
            ),

        "Payment Mode":
            payment_mode,

        "Delivery Status":
            delivery,

        "Supplier Name":
            supplier_name,

        "Supplier Email":
            supplier_email,

        "Stock Left":
            stock_left,

        "Reorder Point":
            reorder_point,

        "Auto Reorder":
            auto_reorder,

        "Reorder Quantity":
            reorder_quantity
    })


# ---------------------------------------------------------
# CREATE DATAFRAME
# ---------------------------------------------------------

df = pd.DataFrame(
    records
)


# ---------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------

print(df.head())

print(
    "\nTotal Orders:",
    len(df)
)

print(
    "Unique Customers:",
    df["Customer Id"].nunique()
)

print(
    "Unique Products:",
    df["Product Id"].nunique()
)

print(
    "Unique Suppliers:",
    df["Supplier Name"].nunique()
)

print(
    "Products to Reorder:",
    df.loc[
        df["Auto Reorder"] == "Yes",
        "Product Id"
    ].nunique()
)


# ---------------------------------------------------------
# SAVE DATASET
# ---------------------------------------------------------

try:

    df.to_csv(
        "Superstone_Management_System.csv",
        index=False
    )

    print(
        "\nDataset generated Successfully!"
    )

    print(
        "File saved as "
        "'Superstone_Management_System.csv'"
    )
    

except PermissionError:

    print(
        "Please close the file "
        "'Superstone_Management_System.csv' "
        "if it is open in Excel or Power BI."
    )