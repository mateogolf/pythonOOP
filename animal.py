class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "{}'s health: {}".format(self.name,self.health)

animal = Animal("Tiger",250)
#walk() three times, run() twice, and finally displayHealth()
animal.walk().walk().walk()
animal.run().run()
animal.displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name,150)
    def pet(self):
        self.health += 5
        return self

GSD = Dog("Justin")
#walk() three times, run() twice, and finally displayHealth()
GSD.walk().walk().walk()
GSD.run().run()
GSD.pet()
GSD.displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name,170)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"

#creating a new Animal and confirm that it can not call the pet() and fly() methods, and its displayHealth() is not saying 'this is a dragon!'. 
a1 = Animal("Osterich")
# a1.pet()
# a1.fly()
a1.displayHealth()
# #confirm that your Dog class can not fly().
# GSD.fly()