# Demonstrates usage of super() to call parent class constructor

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {name} is created")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"{name} Dog of breed {breed} is created")

dog = Dog("Buddy", "Golden Retriever")


# Demonstrates usage WITHOUT super() to call parent class constructor

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {name} is created")

class Dog(Animal):
    def __init__(self, name, breed):
        # super().__init__(name)
        self.breed = breed
        print(f"{name} Dog of breed {breed} is created")

# Test
dog = Dog("Buddy", "Golden Retriever")

# Note: we can still access the parent class's methods and attributes, like "name"
# However, the constructor of the parent class will not be called, so any initialization done there will be skipped.
# This can lead to issues if the parent class has important initialization logic.