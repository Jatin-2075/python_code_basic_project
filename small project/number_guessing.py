import random
a = int(input("enter any number between 1 to 100 \n"))

def guessing():
    random_comp = random.randint(1 , 100)
    x = random_comp

    while True :
        a = int(input("enter any number between 1 to 100 \n"))     
        if a == x :
            print("you won")
            
        elif a >= x :
            print("think little less")
            
        elif a <= x :
            print("think little big")
guessing()