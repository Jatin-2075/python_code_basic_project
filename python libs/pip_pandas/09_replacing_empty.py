import pandas as pd
df = pd.read_csv('data.csv')

df.fillna(69, inplace = True)
print(df)