a = float(input("enter the number you want "))
b = float(input("enter the second number you want "))
n = input("enter the maths function you want to do \n only from add(i), subtract(j), multiply(k), divide(l), percentage(m)\n")

i = [a+b]
j = [a-b]
k = [a*b]
l = [a / b]
m = [a % b]
def myfunc():
        if n == "i" :
            print(i)
        elif n == "j" :
            print(j)
        elif n == "k" :
            print(k)
        elif n == "l" :
            print(l)
        elif n == "m" :
            print(m)
myfunc()