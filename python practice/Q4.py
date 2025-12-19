import pandas as pd

sales= pd.read_csv('sales_data.csv')

for i in sales['Price']:
    if i > 1500:
        print(i)