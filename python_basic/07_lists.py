list1 = [ "apple" , "banana" , "pineapple" , "cherry" , "strawberry"]
list2 = list(("apple" ,  "banana"))
print(list2)

#  TO ACCESS ITEMS FROM LIST
print(list1[1])

#  TO acees the last  MEMBER FROM LIST 
print(list1[-1])

#   TO JUST ADD A RANGE IN LIST
print(list1[2:5])
#and negavtive index of range works same for this as same as member from list

# to vheck if member is in list 
if "apple" in list1:
    print("yes apple is there")

# TO CHANGE LIST
list1[1] = "blackcurrent"
print(list1)

list1[1:3] = ['litchi' , 'berry']
print(list1)

#to insert item
list2.insert(1 , "watermelon") 
print(list2)

# to add the item at end of list
list2.append("orange")
print(list2)


# to add the 2 list 
seasonal = ['mango' , "grappes"]
list2.extend(seasonal)
print(list2)
# FROM THIS METHOD YOU CAN ADD ANY LIST TUPLE SET TO THE LIST

# REMOVE FROM LIST WE WILL DO THIS
list1.remove("apple")
# more function like this are pop , clear , del , 
print(list1)


# to loop list then we will use while
for x in list1:
    print(list1)


list3 = ['jatin' , 'mohit', 'ritesh']
i = 0
while i < len(list1):
    print(list3)
    i = i + 1