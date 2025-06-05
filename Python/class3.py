class Animal:   #Parent class
    def eat(self):
        print("Eating......")

class Dog(Animal):  #Child class
    def bark(self):
        print("Barking.......")

obj=Dog()

obj.eat()
obj.bark()