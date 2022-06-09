# Operator Overloading/ Magic Methods:

class Book:
    def __init__(self, pages):
        self.pages = pages
    
    def __add__(self, other):
        return self.pages + other.pages
    
    def __mul__(self,other):
        return self.pages * other.pages

b1 = Book(40)
b2 = Book(20)

# object -> b1,b2 && attribute -> 40,20

print(b1 + b2)
print(b1 * b2)