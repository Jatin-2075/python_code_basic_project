import pandas as pd
df = pd.read_csv('data.csv')
# print(df.duplicated())
#another method is 
df.drop_duplicates(inplace = False)
print(df.to_string())