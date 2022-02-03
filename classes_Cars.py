



class Car():
 #"""A simple attempt to represent a car."""
    def __init__(self, make, model, year):
 #"""Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading=0
 
    def get_descriptive_name(self):
# """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("the car has "+str(self.odomoter_reading)+" Left")
    def update_odometer(self,milage):
        if milage>=self.odomoter_reading:
                    self.odomoter_reading=milage
        else:
            print("You cant't roll bakc an meter")
    def increment_odometer(self,miles):
        self.odomoter_reading+=miles
    def fill_gas_tank(self):
        print("This car requires 1gallon of gas per 100km")
            
#my_used_car = Car('subaru', 'outback', 2013)
#print(my_used_car.get_descriptive_name()) 
#my_used_car.update_odometer(23500)
#my_used_car.read_odometer()
#my_used_car.increment_odometer(12312)
#my_used_car.read_odometer()
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_pack=2080
    def describe_battery(self):
        print("This car has a "+str(self.battery_pack)+" which can last 10000miles")
    def fill_gas_tank(self):
        print("This car doesnot requires any gas")
my_tesla=ElectricCar('tesla','model s plaid','2021')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()



