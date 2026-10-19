def my_func(fname):
    print(fname + " code")

my_func("bad")
my_func("good")
my_func("normal")

#   * is used to add parameter and access the names
def my_function(*kids):
    print("the oldest child in class is " , kids[2])

my_function("jatin" , "ritesh" , "mohit")

def my_func(**kids):
    print("the child is in 2nd " + kids["lname"])

my_func(fname = "jatin" , lname = "sharma")


def my_function( a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c = 7 , d = 8)