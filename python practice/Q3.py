import pandas as pd

sales= pd.read_csv('sales_data.csv')
sales_=sales[['Product', 'Price']]
print(sales_)