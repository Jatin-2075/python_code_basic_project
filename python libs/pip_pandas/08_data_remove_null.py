import pandas as pd
# dropna() this removes empty cells
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())

#if we don't want new_df then in bracket type 
#inplace = true 
