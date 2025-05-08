# Printing multiplication table using Python nested for loops
for num in range(3,5):
    for i in range(1,11):
        print(f"{num} * {i} = {i*num}")
    print()

# Using break statement in nested loops
for i in range(2, 4): # Running outer loop from 2 to 3
    for j in range(1, 11):
      if i==j:
        break
      print(i, "*", j, "=", i*j)
    print()

# Using continue statement in nested loops
for i in range(2, 4):
    for j in range(1, 11):
      if i==j:
        continue
      print(i, "*", j, "=", i*j)
    print()

# Single line Nested loops using list comprehension
list1= [[j for j in range(5)] for i in range(3)]
print(list1)