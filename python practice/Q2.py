#CSV Handling
#Write code to read a CSV file named sales.csv and show the first 5 rows.


import pandas as pd

sales = pd.read_csv('sales_data.csv')
print(sales.head())