import pandas as pd
a = [10, 20, 30, 40, 50]
myvar = pd.Series(a)
print(myvar)

print(myvar[0])#this is a label 

#create index custom
my2var = pd.Series(a, index = ["a", "b", "c", "d", "e"])
print(my2var)
print(my2var["a"])

calories = {
    "day1" : "233",
    "day2" : "344",
    "day3" : "234"
}

mycal = pd.Series(calories)
print(mycal)

