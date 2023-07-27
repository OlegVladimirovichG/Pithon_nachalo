class Rectangle:
    def __init__(self, a, b = None):
        self.a = a
        self.b = b
        self.shape = 'rectangle'
        if not b:
            self.b = a
            self.shape = 'square'
        
    def square(self):
        return self.a * self.b

    def perimetr(self):
        return self.a * 2 + self.b * 2


r1 = Rectangle(5, 6)
print(r1.perimetr)
print(r1.square)
print(r1.shape)

r2 = Rectangle(5)
print(r2.perimetr)
print(r2.square)
print(r2.shape)