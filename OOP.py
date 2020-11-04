

class Vehicle:

    # constructor
    def __init__(self, color, price, brand):
        self.color = color
        self.price = price
        self.brand = brand

    def drive(self):
        print("Driving")

    def park(self):
        print("Parking")


# ירושה
class Car(Vehicle):

    def __init__(self, color, price, brand, doors_num):
        super().__init__(color, price, brand)
        self.doors_num = doors_num

    def turnOnRadio(self):
        print("Radio is on")



class Motorcycle(Vehicle):
    def __init__(self, color, price, brand):
        super().__init__(color, price, brand)

    def openWheel(self):
        print("I can to open wheel")



car = Car("red",150000,"Mazda",4)
motorcycle = Motorcycle("white",10000,"mazda")

car.turnOnRadio() # פעולות עושים על המשתנה
motorcycle.openWheel()
