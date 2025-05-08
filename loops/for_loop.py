'''var is the variable name, and iterable is an object which can be looped over or iterated over with the help of a for a loop. 
Objects like tuples, lists, sets, dictionaries, strings, etc. are called iterable. We can also use the range() function in place of iterable.

for var in iterable:

   statements '''

li = ["geeks", "for", "geeks"]
for i in li:
    print(i)
    
tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)
    
s = "Geeks"
for i in s:
    print(i)
    
d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i]))
    
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),