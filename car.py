class Car:
    def __init__(self, model, miles=0, used=False):
        self.model = model
        self.miles = miles
        self.used = used

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_miles(self, miles):
        self.miles = miles

    def add_miles(self, new_miles):
        self.miles += new_miles

    def get_miles(self):
        return self.miles

    def is_used(self):
        return self.used


my_car = Car("Mercedes", 25000, True)
print(my_car.get_model())
print(my_car.get_miles())
print(my_car.is_used())

my_car.add_miles(100)
print(my_car.get_miles())

