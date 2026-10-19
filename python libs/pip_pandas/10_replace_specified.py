import pandas as pd
df = pd.read_csv('data.csv')
df.fillna({"calories" : 69} , inplace=True)
print(df.to_string())