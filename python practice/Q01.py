#DataFrame Creation
#Create a Pandas DataFrame from this dictionary and display it:

import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Marks": [78, 85, 90]
}

df = pd.DataFrame(data)
print(df)
