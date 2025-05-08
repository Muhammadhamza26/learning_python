#### Remove items from Set

# Using remove()
a = {1, 2, 3, 4, 5}

a.remove(5)  
print(a)

# Using discard()
#removes a specified element from a set without raising a KeyError
a = {1, 2, 3, 4, 5}
a.discard(6)
print(a)

# Using pop()
a = {1, 2, 3, 4, 5}
r = a.pop()
print(f"Removed: {r}")
print(a)
r = a.clear()
print(a)

#### Check if two lists have at-least one element common

a = [1, 2, 3, 4]
b = [5, 6, 3, 8]

# Find common elements using set intersection
common = set(a) & set(b)
print(common)
print("Common" if common else "not common")
