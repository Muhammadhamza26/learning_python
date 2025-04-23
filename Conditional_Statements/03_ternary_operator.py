class StringProcessor:
    def __init__(self, sentence):
        self.sentence = sentence

    def capitalize_first(self):
        return self.sentence.capitalize()

    def title_case(self):
        return self.sentence.title()

    def letter_count(self):
        return sum(1 for ch in self.sentence if ch.isalpha())

    def total_chars(self):
        return len(self.sentence)

    def custom_title(self):
        return " ".join(word[0].upper() + word[1:] for word in self.sentence.split())


class LambdaExamples:
    def __init__(self):
        self.s2 = lambda func: " ".join(i[0].upper() + i[1:] for i in func.split())
        self.square_lambda = lambda x: x ** 2

    def square_def(self, x):
        return x ** 2

    def list_comprehension_lambda(self):
        return [lambda func=i: func * 10 for i in range(5)]


class TernaryDemo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compare(self):
        return {True: self.a, False: self.b}[self.a > self.b]


# ----------- Testing the Classes -----------

# StringProcessor demo
s1 = "hello ai world"
sp = StringProcessor(s1)

print("Capitalize:", sp.capitalize_first())
print("Title Case:", sp.title_case())
print("Total letters:", sp.letter_count())
print("Total characters:", sp.total_chars())
print("Custom Title Case:", sp.custom_title())

# LambdaExamples demo
le = LambdaExamples()
print("Lambda title case:", le.s2(s1))
print("Lambda square of 3:", le.square_lambda(3))
print("Def-based square of 3:", le.square_def(3))

print("Lambda with list comprehension (x10):")
for fn in le.list_comprehension_lambda():
    print(fn())

# TernaryDemo
td = TernaryDemo(20, 30)
print("Ternary result:", td.compare())
