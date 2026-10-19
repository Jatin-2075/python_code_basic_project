data = {
    'a': "Hello World",
    'b': 20,
    'c': 20.5,
    'd': 1j,
    'e': ["apple", "banana", "cherry"],  # list   duplicate member and changeable
    'f': ("apple", "banana", "cherry"),  # TUPLE  unchangeabke allow duplicate member
    'g': range(6),
    'h': {"name": "John", "age": 36},  # DICT changeable and no duplicate member
    'i': {"apple", "banana", "cherry"},  # set no duplicate and no unchangeabke
    'j': frozenset({"apple", "banana", "cherry"}),
    'k': True,
    'l': b"Hello",
    'm': bytearray(5),
    'n': memoryview(bytes(5)),
    'o': None
}


for x in data:
    y = data.get(x)
    print(x , "for an example of " , type(y))

char = input("Enter a character:\n (or you enter stop to exit)\n")

if char in data:
    data_type = type(data[char])
    value = data[char]

    print(f"Data type of '{char}': {data_type}")
    print(f"Value of    '{char}': {value}")
    
else:
    print(f"Character '{char}' not found in data.")
    