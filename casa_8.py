import pandas as pd

data = "big-mac-full-index.csv"
df = pd.read_csv(data)

# Iterating over rows
for index, row in df.iterrows():
    total_sales = row['Quantity'] * row['Price']
    print(f"{row['Item']} Total Sales: ${total_sales}")


data = "big-mac-full-index.csv"
df = pd.read_csv(data)
# Defining a function to calculate total sales for each row
def calculate_total_sales(row):
    return f"{row['Item']} Total Sales: ${row['Quantity'] * row['Price']}"

# Applying the function row-wise
result = df.apply(calculate_total_sales, axis=1)
for res in result:
    print(res)
