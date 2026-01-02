#Column #Selection
#From a DataFrame df, write code to select only the columns "Name" and "Salary".

import pandas as pd

sales= pd.read_csv('sales_data.csv')
sales_=sales[['Product', 'Price']]
print(sales_)