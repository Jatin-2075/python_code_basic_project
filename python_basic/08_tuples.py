# in tuples we have to enter atleast 1 , so that it is tuple and don not become str 
t = ("apple",)
print(type(t))
# tuples cannot be edited added or removed like wise in list 

#we can actually make a tuple using tuple()
u = tuple(("apple" , "banana"))
print(u)


#access tuple items 
print(t[0])

# negative means the items from lst not from starting and ranges are same in tuples like list
# to check if it exist 
if "apple" in t:
    print("yes")

# to update tuple we can actually change it in list and then in tuples 
x  = ("banana" , "apple" , "kiwi")
y = list(x)
y[1] = "lemon"
x = tuple(y)
print(x)

# to add item we can use append 
y = list(x)
y.append("orange")
x = tuple(y)
print(x)

#we can add remove same like lists in tuple 

# to unpack it we can do this 
fruits = ("apple" , "banana" , "cherry" , "strawberry")
(green , yellow , *red) = fruits
print(green)
print(yellow)
print(red)