# Multi level inheritance
class Animal:   #Parent class
    def eat(self):
        print("Eating......")

class Dog(Animal):  #Child class
    def bark(self):
        print("Barking.......")

class Puppies(Dog):  #Child class
    def weap(self):
        print("Weaping.....")
    #Method overriding 
    def eat(self):
        print("Drinking Milk.....")

obj=Puppies()
obj.eat()
obj.bark()
obj.weap()

a=Animal()
a.eat()