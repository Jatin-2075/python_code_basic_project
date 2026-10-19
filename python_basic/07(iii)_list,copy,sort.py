list1 = ['mango' , 'apple' , 'banana' , 'orange' , 'kiwi']
list1.sort()
print(list1)

# same with number
list2 = [100, 92 , 28 , 78 , 92]
list2.sort()
print(list2)

# sort by decending
list1.sort(reverse = True)
print(list1)

#same with number
list2.sort(reverse=True)
print(list2)

# to see which number is closest to number line 
def myfunc(n):
    return abs(n - 50)
list3 = [23 , 73 , 89 , 90 , 100 , 50]
list3.sort(key= myfunc)
print(list3)

#if you want to reverse the list
list1.reverse()
print(list1)

#lets copy the lists 
list5 = list1.copy()
print(list5)
#this can be done by other method like 
# using list5 = list(list1)
#same as list5 = list1[:]

# we can add 2 list by these methods 
list6 = list1 + list2
print(list6)

for x in list2:
    list1.append(x)

print(list1)

list3.extend(list2)
print(list3)
