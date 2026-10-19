#string format 
age = 19
name = " jatin "
print(age , name)

#another method used is by specifiying the string 
# actualy f specifies that this a string 
name2 = f"my name is jatin and my age is {age}"
print(name2) 

# lets suppose if anything in integer have decimak thenn use '.2f' ':'
price = 90.00
material = f" this tshirt costs you around {price:.2f} dollars"  
print(material)

 # and we can actualy multiply number in string itself
t = f"this is the price of tshirt {23 * 89}"
print(t)