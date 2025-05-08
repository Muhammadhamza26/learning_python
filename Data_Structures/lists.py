
my_list = [1, 2, 3, 4, 5]

# Interchange first and last elements
my_list[0], my_list[-1] = my_list[-1], my_list[0]

print("List after swapping first and last elements:", my_list)


# check if string is palindrome
s = "absaaba"
a = list(s) == reversed(s)

print("palindrome" if a == s else "not palindrome")
print("palindrome2" if s == s[::-1] else "not palindrome2" )

half = len(s)//2 
print("symmetrical" if s[:half] == s[half:] else "Not symmetrical")