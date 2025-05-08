# Swap function
def swapList(list):
    
    get = list[-1], list[0]
    
    # unpacking those elements
    list[0], list[-1] = get
    
    return list
    
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))


# Swap first and last values in a list in Python using * operand
# Swap function
def swapList(list):
    
    start, *middle, end = list
    list = [end, *middle, start]
    
    return list
    
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


# Swap first and last values in a list in Python using Slicing

def swap_first_last_3(lst):
    if len(lst) >= 2:
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst

inp=[12, 35, 9, 56, 24]

print("The original input is:",inp)

result=swap_first_last_3(inp)
print("The output after swap first and last is:",result)