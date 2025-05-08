#### Handling Missing keys in Python Dictionaries Using key
country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

print(country_code.get('India', 'Not Found'))
print(country_code.get('Japan', 'Not Found'))



#### Dictionaries Using the try-except block
country_code = {'India': '0091',
				'Australia': '0025',
				'Nepal': '00977'}

try:
	print(country_code['India'])
	print(country_code['USA'])
except KeyError:
	print('Not Found')

#### Sort and print
d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

myKeys = list(d.keys())
myKeys.sort() # Sorted Dictionary
sd = {i:d[i] for i in myKeys}
print(sd)

#### Sort and print
d = {2: 56, 1: 2, 5: 12, 4: 24}

print("Dictionary", d)
for i in sorted(d.keys()):
    print(i, end=" ")
print()


### Sorting Dictionary By Value using Numpy
# Creates a sorted dictionary (sorted by key)
import numpy as np

d = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

keys = list(d.keys())
values = list(d.values())
sorted_value_index = np.argsort(values) # return indices that sorts an array 
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
print(sorted_dict)

##### find the sum of all items in a dictionary
d = {'a': 100, 'b': 200, 'c': 300}

res = sum(d.values())
print(res)

