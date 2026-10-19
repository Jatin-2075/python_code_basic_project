import pandas as pd
mylist = {
    "car" : ["lambo", "bmw", "bugatti"],
    "year": [2019, 2022, 2021]
}

mylist = pd.DataFrame(mylist)
print(mylist)