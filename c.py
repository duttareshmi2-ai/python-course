class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def move(self):
        print("Car is driving")

# Example
c = Car("Toyota", "Corolla")
c.move()
print(issubclass(Car, Vehicle))
