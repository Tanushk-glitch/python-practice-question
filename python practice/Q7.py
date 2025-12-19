#Handling Missing Values
#How will you replace NaN values with 0 in a DataFrame?


import pandas as pd

data = pd.read_csv('sample_data_40.csv')
new_data = data.fillna({"Age":20})
#print(new_data)

print(new_data.to_string())