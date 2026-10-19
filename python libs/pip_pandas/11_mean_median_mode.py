import pandas as pd
df = pd.read_csv('data.csv')
x = df["calories"].mean()
df.fillna({"calories" : x} , inplace = True)
print(df.to_string())
#change median or mode to mean and it will work same 