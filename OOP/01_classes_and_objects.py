# Demonstrates basic classes, objects, and instance methods

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

    def __str__(self):
        return f"{self.name} is a {self.age} year old dog."

# Creating and using an object
dog1 = Dog("Buddy", 3)
dog1.bark()
print(dog1)

