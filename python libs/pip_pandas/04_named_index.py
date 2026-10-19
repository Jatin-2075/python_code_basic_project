import pandas as pd
data = {
    "calories" : [324, 423, 524],
    "duration" : [60, 64, 80]
}

df = pd.Dataframe(data , index = ["day1" , "day2", "day3"])
print(df)
print(df.loc["day2"])