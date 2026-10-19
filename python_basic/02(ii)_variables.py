x = 'nice'

def myfunc():
    x = "awesome"
    print("python is", x)

myfunc()

print("when global is not used till now the x is ", x)

def myfunc():
    global x
    x = "fantastic"
myfunc()

print("when global function is used",x)
print(x)