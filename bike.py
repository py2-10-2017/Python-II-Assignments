#Create a new class called Bike with the following properties/attributes:
#price, max_speed, miles

class Bike(object):
    #Use the __init__() function to specify the price and max_speed of each instance
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        #displayInfo() - have this method display the bike's price, maximum speed,
        #and the total miles.
        print "Price: $" + self.price
        print "Max speed: " + self.max_speed + " mph"
        print "Mileage: " + str(self.miles) + " miles"

    def ride(self):
        #ride() - have it display "Riding" on the screen and increase the total
        #miles ridden by 10
        print "Riding..."
        self.miles += 10

    def reverse(self):
        #everse() - have it display "Reversing" on the screen and decrease the
        #total miles ridden by 5
        print "Reversing..."
        #Prevent negative mileage w/ "if" statement
        if self.miles >= 5:
            self.miles -= 5

#Create 3 instances of the Bike class
bike1 = Bike("300", "18")
bike2 = Bike("150", "10")
bike3 = Bike("275", "20")

#Have the first instance ride three times, reverse once
#and have it displayInfo().
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

#Have the second instance ride twice, reverse twice
#and have it displayInfo().
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

#Have the third instance reverse three times and displayInfo().
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()
