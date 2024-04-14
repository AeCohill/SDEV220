class Vehicle():
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

class Automobile(Vehicle):
    def __init__(self, make, model, year, is_2door, has_sunroof):
        super().__init__("Automobile")
        self.make = make
        self.model = model
        self.year = year
        self.is_2door = is_2door
        self.has_sunroof = has_sunroof

def main():
    vehicleType = 'car'
    make = input('Input maker of your vehicle: ')
    model = input('Input the model of your vehicle: ')
    year = input('Input the year of your vehicle: ')
    is_2door = input('Is your vehicle a 2_door? Enter True/False: ').lower() == 'true'
    has_sunroof = input('Does it have a sunroof? Enter True/False: ').lower() == 'true'
    
    my_Automobile = Automobile(make, model, year, is_2door, has_sunroof)
    
    print("\nCar Details:")
    print("\nMake: ",my_Automobile.make)
    print("\nModel: ",my_Automobile.model)
    print("\nYear: ",my_Automobile.year)
    print("\nyour car Is a 2 door vehicle:",my_Automobile.is_2door)
    print("\nYour car has a sunroof:", my_Automobile.has_sunroof )
    
if __name__ == "__main__":
    main()            