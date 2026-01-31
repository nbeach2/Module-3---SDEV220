#Noah Beach
#Filename: M3Lab.py
#Descrption: This program defines a Vehicle class and an Automobile subclass. It prompts the user for an input of automobile details and displays the information.
#List and Description of variables:
#   vehicle_type - stores the type of vehicle
#   year - stores the year of the car
#   make - stores the make of the car
#   model - stores the model of the car
#   doors - stores the number of doors of the car
#   roof - stores the type of roof of the car
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
def main():
    year = input("Enter the year:")
    make = input("Enter the make:")
    model = input("Enter the model:")
    doors = input("Enter the number of doors (2 or 4):")
    roof = input("Enter the type of roof (solid or sun roof):")
        
    car = Automobile(year, make, model, doors, roof)
    print("\nVehicle type:", car.vehicle_type)
    print("Year:", car.year)
    print("Make:", car.make)
    print("Model:", car.model)
    print("Number of doors:", car.doors)
    print("Type of roof:", car.roof)

main()