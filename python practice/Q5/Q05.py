#Add New Column
#Add a new column "Discounted_Price" to df which is 10% of Price.


import pandas as pd

sales =pd.read_csv('sales_data.csv')
sales["Discounted_Price"] = sales["Price"] * 0.9
sales_ = sales[[ 'Price', 'Discounted_Price']]    
print(sales_)
