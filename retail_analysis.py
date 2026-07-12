import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
print("project started successfully!")
os.makedirs("images", exist_ok=True)

# Load dataset
df = pd.read_csv("Superstore.csv", encoding="latin1")

print("Dataset Shape:", df.shape)

# Basic Information
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Monthly Sales Trend
monthly_sales = df.groupby(
    df["Order Date"].dt.month
)["Sales"].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("images/monthly_sales_trend.png")
plt.show()

# Category Sales
plt.figure(figsize=(8,5))
sns.barplot(
    data=df,
    x="Category",
    y="Sales"
)
plt.title("Sales by Category")
plt.savefig("images/sales_by_category.png")
plt.show()

# Profit Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Profit"], bins=30)
plt.title("Profit Distribution")
plt.savefig("images/profit_distribution.png")
plt.show()

# Correlation
numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(), annot=True)

plt.title("Correlation Heatmap")
plt.savefig("images/correlation_heatmap.png")
plt.show()

print("\nProject Completed Successfully!")