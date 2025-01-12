class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f'make: {self.make}, model: {self.model}'


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f'make: {self.make}, model: {self.model}, fuel_type: {self.fuel_type}'

A = Vehicle('q', 'm')
B = Car('q', 'm', '92')
print(A.get_info())
print(B.get_info())