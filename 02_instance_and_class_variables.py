# Demonstrates class variables vs. instance variables

class Car:
    # Class Variable
    vehicle = 'car'

    def __init__(self, model):
        self.model = model  # Instance Variable

    def set_price(self, price):
        self.price = price  # Instance Variable

    def get_price(self):
        return self.price

# Object creation
audi = Car("R8")
audi.set_price(1000000)
print(audi.get_price())
print(audi.vehicle)  # Accessing class variable

# Deleting a method is generally not recommended, but for demo:
# del audi.set_price
# print(audi.get_price())  # This will raise an error
