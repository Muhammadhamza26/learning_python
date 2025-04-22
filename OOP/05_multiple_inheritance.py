# Demonstrates multiple inheritance with method resolution order (MRO)

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

# Test
c = C()
c.pro()
