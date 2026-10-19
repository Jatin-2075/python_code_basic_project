import random
password = "zxcvbnmlkjhgfdsaqwertyuiop@#$&1234567890ABCDEFGHIJKLMNOPQURSTUVWXYZ"
length_password = int(input("enter the length of the password "))
a = "".join(random.sample(password , length_password))
print(f"passwrod is : {a}")