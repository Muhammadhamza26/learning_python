# Using split() and join()
s = "Geeks for Geeks-1"

# Split the string into words, reverse the list of words, and join them back
reversed_words = ' '.join(s.split()[::-1])

print(reversed_words)

# Using enumerate function to get the length of the string
a = "geeks"
s = 0

for i, a in enumerate(a):
  # Increment 's' by 1 for each character in the string
    s += 1
print(s)


# print even length words in a string
s = "This is a python language"

# split the sentence into words
wrds = s.split()

# filter words with even length
even_wrds = [w for w in wrds if len(w) % 2 == 0]

# Join the filtered words back into a sentence
res = " ".join(even_wrds)
print(res)

# Using a for loop to remove letters from a string
s = "hello world"
s = "".join([i for i in s if i != "w"]) # with list comprehension 
c = ""
for i in s:
    if i != "w":
        c += i
print(s, c) 