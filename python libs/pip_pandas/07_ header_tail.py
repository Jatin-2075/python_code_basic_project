import pandas as pd
#header are just use to get over view and have 5 rows if nothing is their
df = pd.read_csv('data.csv')
print(df.head(10))

#tail is used to view last rows

print(df.tail())

#to get info of  data
print(df.info())