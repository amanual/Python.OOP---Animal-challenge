# #creating inheritance animal class challenge
class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):        
        self.health -= 5
        return self
    def display_health(self):
        print "My name is:",self.name
        print "Health:", self.health
        

animal1 = Animal("Lion", 100)
animal1.walk().walk().walk().run().run().display_health()   

#Dog class begins here
class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(self, name)
        self.health = 150
        self.name = name

    def pet(self):
        self.health += 5        
        return self

dog1 = Dog("dog", 200)
dog1.walk().walk().walk().run().run().pet().display_health()

#Dragon class begins here
class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(self, name)
        self.health = 170
        self.name = name

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print "I am a Dragon"
        super(Dragon, self).display_health()

dragon1 = Dragon("Dragon", 300)
dragon1.fly().display_health()      

# dog1.fly() -- dog can't fly since fly is not defined inside the dog class
# dragon1.pet() -- dragon can't fly since fly is not defined inside the dog class

