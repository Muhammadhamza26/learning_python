# topics covered in this code:
# - Object-Oriented Programming (OOP)
# - Classes and Objects
# - Inheritance
# - Constructors and Instance Variables
# - Class Variables and Instance Variables

# class Dog:
#     def __init__(self, name, age):  
#         self.name = name 
#         self.age = age

#     def bark(self): 
#         print(f"{self.name} is barking!")

#     def __str__(self):
#         return f"{self.name} is a {self.age} year old dog."

# # Creating an instance of Dog
# dog1 = Dog("Buddy", 3)
# dog1.bark() 
# print(dog1)


# # Another example of OOP in Python
# # This example demonstrates the concept of classes and objects in Python.
	
# class Car: 
		
# 	# Class Variable 
# 	vehicle = 'car'
		
# 	# The init method or constructor 
# 	def __init__(self, model): 
			
# 		# Instance Variable 
# 		self.model = model			 
	
# 	# Adds an instance variable 
# 	def setprice(self, price): 
# 		self.price = price 
		
# 	# Retrieves instance variable	 
# 	def getprice(self):	 
# 		return self.price	 
	
# # Driver Code 
# Audi = Car("R8") 
# Audi.setprice(1000000) 
# print(Audi.getprice()) 

# Deleting an Object in Python:
# del Audi.setprice # Deleting the setprice method
# print(Audi.getprice())


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound."

# # Child class inherits from Animal
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"
#         # It allows the child class to override a method defined in the parent class.

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# # Test
# animals = [Dog("Rex"), Cat("Milo")]

# for a in animals:
#     print(a.speak())

## super() function in OOP
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print(f"Animal {name} is created")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#         print(f"{name} Dog of breed {breed} is created")
# dog = Dog("Buddy", "Golden Retriever")


#### Multiple Inheritance Scenario
class A:
    def process(self):
        print("Processing in A")

class B(A):
    def process(self):
        super().process()
        print("Processing in B")

class C(B):
    def pro(self):
        super().process()
        print("Processing in C")

c = C()
print(c.pro()) 

