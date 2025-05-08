# cnt = 0
# while (cnt < 3):
#     cnt = cnt + 1
#     print("Hello Geek")
# else:
#     print("In Else Block")


fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)  # Get an iterator from the list

while True:
    try:
        fruit = next(iter(fruits))  # Get the next item from the iterator
        print(fruit)            # Print the current fruit
    except StopIteration:       # Raised when there are no more items
        break                   # Exit the loop
