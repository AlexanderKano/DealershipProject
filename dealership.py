class Dealership:

    def __init__(self, employees=None, cars=None, revenue=0):
        self.employees = employees if employees is not None else []
        self.cars = cars if cars is not None else []
        self.revenue = revenue
    
    def revenue(self):
        return self.revenue
    
    def add_car(self, number, used):
        