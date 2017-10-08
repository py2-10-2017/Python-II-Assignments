class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        if price < 10000:
            self.tax = 0.12
        else:
            self.tax = 0.15
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()

    def display_all(self):
        print "Price: $" + str(self.price)
        print "Speed: " + str(self.speed) + " mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + " miles"
        print "Tax: " + str(self.tax)

car1 = Car("15000", "110", "Empty", "3400")
car2 = Car("26500", "125", "Full", "9700")
car3 = Car("9400", "115", "Half Tank", "11000")
car4 = Car("31600", "108", "Quarter Tank", "13000")
car5 = Car("23000", "111", "Full", "5000")
car6 = Car("7600", "160", "Empty", "19000")
