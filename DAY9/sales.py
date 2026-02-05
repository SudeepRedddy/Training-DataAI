import pandas as pd

df = pd.read_csv("sales.csv")
print("Sales Data:")
print(df)

df["total_sales"] = df["price"] * df["quantity"]


total_sales_per_product = df.groupby("product")["total_sales"].sum()
print("\nTotal Sales Per Product:")
print(total_sales_per_product)

best_by_quantity = df.groupby("product")["quantity"].sum().idxmax()
print("\nBest Selling (Most Quantity Sold):", best_by_quantity)

df["tax_20_percent"] = df["total_sales"] * 0.20

print("\nFinal Data:")
print(df)