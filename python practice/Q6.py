import pandas as pd

data = pd.read_csv('sales_data.csv')

total_sales = data.groupby('Category')['Price'].sum()
print("Total Sales:", total_sales)