Superstone Management System -- Data Analysis

📌 Project Overview

Superstone Management System -- Data Analysis is an end-to-end data
analytics project built to analyze business data across sales,
products, inventory, customers, and regions.

The project follows a practical analytics workflow: data generation →
data validation and cleaning → exploratory data analysis → visualization
→ business insights → Power BI dashboarding.

Python was used for data analysis and visualization with Pandas,
NumPy, Matplotlib, and Seaborn, while Power BI was used to build
an interactive dashboard for business reporting and decision-making.

Note: The dataset is synthetic and was created for learning and
project demonstration purposes. It does not represent real company
data.

🎯 Business Objective

The project aims to answer business-oriented questions such as:

How are sales performing across regions and products?

Which products contribute strongly to sales?

Which products have high inventory value relative to their sales?

Which products currently have low stock and may require
replenishment attention?

How does inventory value vary across product categories and states?

What patterns can be identified from customer and sales data?

How can these findings support better business decisions?

📂 Dataset

The dataset was self-created using Python to simulate a realistic
business management scenario.

It contains information related to:

Products

Categories

Sales

Customers

Regions / States

Inventory

Stock levels

Reorder points

The dataset was created specifically to practice the complete data
analytics workflow without using confidential or real-world company
data.

🔄 Project Workflow

1. Data Generation & Understanding

The initial dataset was generated using Python and then inspected to
understand:

Dataset dimensions

Column names

Data types

Missing values

Duplicate records

Basic statistical information

Potential data-quality issues

2. Data Cleaning & Validation

The data was checked and prepared for analysis by:

Checking missing values

Checking duplicate records

Verifying data types

Reviewing numerical fields

Validating the consistency of important business columns

The goal was to make the dataset reliable enough for analysis and
dashboard development.

3. Exploratory Data Analysis (EDA)

EDA was performed using Pandas and NumPy to examine:

Sales performance

Product performance

Regional performance

Inventory levels

Customer-related patterns

Category-level performance

4. Data Visualization

Matplotlib and Seaborn were used to create visualizations for:

Product comparisons

Regional comparisons

Sales patterns

Category distributions

Inventory-related analysis

Relationships between business metrics

5. Power BI Dashboard

The important findings from the analysis were presented through an
interactive Power BI dashboard.

The dashboard contains dedicated views for:

Home

Sales

Inventory

Customers

Interactive filters such as date range and month selection allow
users to explore the data dynamically.

🛠️ Tech Stack

Tool / Technology   Purpose

Python          Data generation, cleaning and analysis
Pandas          Data manipulation and EDA
NumPy           Numerical analysis
Matplotlib      Data visualization
Seaborn         Statistical visualization
Power BI        Interactive dashboard and reporting
Git             Version control
GitHub          Project hosting and portfolio

📊 Key Analysis Areas

💰 Sales Analysis

Sales data was analyzed to understand:

Product-level sales performance

Regional sales differences

Sales contribution of individual products

Relationship between sales performance and inventory value

📦 Inventory Analysis

Inventory analysis focused on understanding:

Current stock levels

Reorder points

Sales quantity

Low-stock products

Inventory value by category

Inventory distribution by state

Inventory decisions were based on observed data patterns rather than
introducing an arbitrary stock threshold that was not provided by the
business.

👥 Customer Analysis

Customer data was explored to understand:

Customer distribution

Customer-related sales patterns

Differences across business segments

🌎 Regional Analysis

Regional and state-level data was analyzed to identify differences in:

Sales performance

Inventory distribution

Business contribution

💡 Key Business Insights

The analysis produced several business-oriented findings.

1. Sales vs Inventory Value

The comparison of inventory value and total sales helps identify
products that deserve different types of attention.

For example, Notebook and Mouse show strong sales performance relative
to their inventory value, making their stock availability important to
monitor.

On the other hand, products such as Calculator, Bookshelf, and Sofa
have comparatively higher inventory value, so additional investment in
these products should be evaluated against their sales contribution
rather than automatically increasing stock.

2. Low-Stock Products

The inventory dashboard identified five low-stock products:

Product           Stock Left   Reorder Point   Sales Quantity

Cooking Oil               13              25              692
Laptop                    15              31              315
Office Chairs             11              32              273
Rice Bag                  15              28              731
Stapler                   14              31              251

These products should be monitored for replenishment, with priority
influenced by both remaining stock and sales activity.

For example, Rice Bag and Cooking Oil have relatively high sales
quantities while their current stock is below the displayed reorder
point, making them particularly important to monitor.

3. Inventory Concentration

Inventory value is distributed unevenly across product categories. This
helps identify where a significant amount of business capital is tied up
in inventory and where inventory investment should be monitored more
closely.

4. Regional Differences

Regional analysis highlights differences in business performance and
inventory distribution, allowing stronger and weaker-performing areas to
be compared.

📈 Power BI Dashboard

The Power BI report provides an interactive business view of the
analysis.

Dashboard Pages

Home --- Overall business KPIs and summary

Sales --- Sales and product/region performance

Inventory --- Stock, reorder points, sales quantity and
inventory value

Customers --- Customer-related analysis

Inventory Dashboard

The inventory page includes:

Total Stock

Inventory Value

Items in Stock

Low Stock Items

Auto Reorder Items

Date Range filter

Month filter

Reorder Point of Products

Low Stock Items table

Top 5 Products by Stock Value

Inventory Value by Category

Inventory Value by State

📁 Project Structure

Superstone-Management-System-Data-Analysis/
│
├── Dataset/
│   ├── Superstone_Management_System.csv
│   └── data_generator.py
│
├── Power BI/
│   └── Superstone_Management_System_Report.pbix
│
├── Python-Analysis/
│   ├── EDA Superstone.ipynb
│   └── superstone_eda_analyis_summary.csv
│
├── .gitignore
├── README.md
└── requirements.txt

▶️ How to Run the Python Analysis

1. Clone the repository

git clone https://github.com/ayushijoshi3010/Superstone-Management-System-Data-Analysis.git

2. Open the project folder

cd Superstone-Management-System-Data-Analysis

3. Install the required libraries

pip install -r requirements.txt

4. Open the Jupyter Notebook

jupyter notebook

Then open:

Python-Analysis/EDA Superstone.ipynb

📦 Requirements

The Python analysis uses:

pandas
numpy
matplotlib
seaborn

These dependencies are also listed in requirements.txt.

📊 Power BI File

The Power BI report is available at:

Power BI/Superstone_Management_System_Report.pbix

GitHub may not display a preview of the .pbix file in the browser
because it is a binary Power BI file. The file can be downloaded and
opened using Power BI Desktop.

🎓 Key Learnings

This project provided hands-on practice with the complete data analytics
workflow.

Key learnings include:

Data generation using Python

Data cleaning and validation with Pandas

Exploratory Data Analysis

Data visualization using Matplotlib and Seaborn

Product and regional performance analysis

Inventory and replenishment analysis

Translating analytical findings into business insights

Building interactive Power BI dashboards

Using Git and GitHub for project version control

A key lesson from the project was that business conclusions should be
supported by the available data rather than by arbitrary assumptions.

🚀 Future Improvements

Possible future improvements include:

Adding more historical data for stronger time-series analysis

Implementing automated dashboard refresh

Adding customer segmentation

Developing demand forecasting when sufficient historical data is
available

Connecting Power BI to a database instead of a static CSV

Adding more detailed inventory optimization based on defined
business rules

👩‍💻 Author

Ayushi Joshi

Data Analytics | Python | Power BI

⭐ Conclusion

The Superstone Management System -- Data Analysis project
demonstrates how raw business data can be transformed into meaningful
insights through data cleaning, exploratory analysis, visualization,
and business intelligence reporting.

By combining Python-based analysis with Power BI, the project
provides both detailed analytical exploration and an interactive
business-focused view of sales, inventory, products, customers, and
regional performance.