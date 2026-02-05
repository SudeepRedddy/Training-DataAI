import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': ['mon', 'tue'],
    'Product': ['laptop', 'phone'],
    'Price': [800, 500],
    'Quantity': [2, 'three'] 
}

df = pd.DataFrame(data)

print("--- Original Data ---")
print(df)

df['Quantity'] = df['Quantity'].replace('three', 3)

df['Quantity'] = pd.to_numeric(df['Quantity'])

print("\n--- Cleaned Data ---")
print(df)

df['Total_Sales'] = df['Price'] * df['Quantity']

product_sales = df.groupby('Product')['Total_Sales'].sum()
print("\n--- Total Sales Per Product ---")
print(product_sales)

best_product = df.loc[df['Total_Sales'].idxmax()]
print(f"\nBest Selling Product: {best_product['Product']} (Sales: {best_product['Total_Sales']})")

plt.figure(figsize=(6, 4))
plt.bar(df['Day'], df['Total_Sales'], color='purple', edgecolor='black')
plt.xlabel('Day')
plt.ylabel('Total Sales')
plt.title('Total Sales by Day')
plt.show()