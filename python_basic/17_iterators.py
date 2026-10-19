#iterator is a func used to  get item of any tuple list or string
#iter() is used to create an iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))       
print(next(myit))

string1 = "banana"
for x in string1:
    print(x)