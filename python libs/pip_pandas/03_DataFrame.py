import pandas as pd
data = {#2 dimensional data frame 
    "calories" : [234, 543, 534],
    "duration" : [50 , 40 , 45]
}

df = pd.DataFrame(data)
#loc is used to locate 
print(df.loc[0])

print(df.loc[0 ,1])
