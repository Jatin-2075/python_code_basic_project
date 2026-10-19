import json

x = {
    "name" : "jatin",
    "age" : "19",
    "married" : "true",
    "divorced" : "false",
    "childern" : ("ann", "billy"),
    "pets" : None,
    "cars" : [
        {"model" : "bmw m3", "horsepower" : "890",
         "model" : "lambo" , "horsepower" : "1000"}
    ]
} 

print(json.dumps(x))