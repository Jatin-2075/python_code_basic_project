number = int(input("Enter a number: "))
def check_positive(number):
    if number < 0:
        raise ValueError("The number is negative")
    return number

try:
    result = check_positive(number)
except ValueError as e:
    print(e)