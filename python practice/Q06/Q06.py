# GroupBy Operation
#Write Pandas code to find the total sales per category from columns:
#Category
#Price


import pandas as pd

data = pd.read_csv('sales_data.csv')

total_sales = data.groupby('Category')['Price'].sum()
print("Total Sales:", total_sales)
