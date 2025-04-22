# Demonstrating basic Inheritance and method overriding in Python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Testing the overridden speak method
animals = [Dog("Rex"), Cat("Milo")]

for animal in animals:
    print(animal.speak())
