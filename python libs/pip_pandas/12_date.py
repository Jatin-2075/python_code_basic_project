import pandas as pd 
df = pd.read_csv('data.csv')
df['date'] = pd.to_datetime(df['date'], format = 'mixed')
print(df.to_string())