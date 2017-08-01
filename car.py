class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.taxes()
    def display_all(self):#display all
        # print self.__dict__
        # for attr, value in self.__dict__.iteritems():
        #     print "{}: {}".format(attr,value)
        print "Price: {}".format(self.price)
        print "Speed: {}mph".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}mpg".format(self.mileage)
        print "Tax: {}".format(self.tax)
        return self
    def taxes(self):
        if self.price > 10000:
            self.tax=0.15
        else:
            self.tax=0.12
        return self

car1 = Car(2000, 35, "Full", 15)
car1.display_all()

car2 = Car(2000,5, "Not Full",105)
car2.display_all()

car3 = Car(2000,15, "Kind of Full",95)
car3.display_all()

car4 = Car(2000,25, "Full",25)
car4.display_all()

car5 = Car(2000,45, "Empty",25)
car5.display_all()

car6 = Car(20000000,35, "Empty",15)
car6.display_all()