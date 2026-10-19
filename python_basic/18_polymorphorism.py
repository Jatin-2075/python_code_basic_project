class vehicles:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class car(vehicles):
    def move(self):
        print("move!")
    
class boat(vehicles):
    def move(self):
        print("float!")
    
class plane(vehicles):
    def move(self):
        print("fly!")

        
car1 = car("Toyota", "Corolla")
boat1 = boat("Yamaha", "WaveRunner")
plane1 = plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.model)
    print(x.brand)
    x.move()