import pandas as pd
df = pd.read_csv['data.csv']  
df.loc[7, 'duration'] = 45
print(df.to_string())