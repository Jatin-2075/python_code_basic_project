#this work like a filter
list = [ 'apple' , 'mango' , 'strawberry' , 'orange' , 'kiwi']
newlist = []

for x in list:
    if "a" in x :
        newlist.append(x)

print(newlist)

newlist2 = [x for x in list if "a" in x]
print(newlist2)

newlist3 = [ x for x in list if x != "apple"]
print(newlist3)