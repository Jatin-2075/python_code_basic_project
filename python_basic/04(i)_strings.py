#string is a line assign to a variables n
a = "this is my code got it boy "
print(a)

# def my func is not neended here just typed do that i look cool

# if i want a value from a string we will use this method
def myfunc():
   print(a[3])
myfunc()

# to get value from any string we will use this method
def myfunc():
   for x in a:
     print(x)
myfunc()

 # to length of a string 
def myfunc():
   print(len(a))
myfunc()

 # to check if anything is in string or not we will use this method
def myfunc():
   print("code" in a )
myfunc()

# slicing a part from a strimg 
def myfunc():
   print(a[2:8])
myfunc()

# slicning form starting 
def myfunc():
   print(a[:9])
myfunc()

# want to sice from ending 
def myfunc():
   print(a[9:])
myfunc()

# want to remove a part from a string 
def myfunc():
   print(a[-6:-18])
myfunc()

# if i want to modify the string
def myfunc():
   print(a.lower())
   print(a.capitalize())
   print(a.strip())  # this acutaly do nothing but only removes the spaces from start to end
   print(a.replace("code" , "me"))
   print(a.split("code"))
myfunc()

b = " hello"
c = "bot"
print(b +' '+ c)