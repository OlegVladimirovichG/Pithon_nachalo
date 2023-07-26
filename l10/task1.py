import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def len_circ(self):
        return 2 * math.pi * self.radius
    
    def square(self):
        return math.pi * self.radius ** 2
    
    @classmethod
    def square_to_circ(cls, square):
        return cls((square / math.pi) **0.5)
    

c1 = Circle.square_to_circ(10)
print(c1.len_circ())
print(c1.square())
print(c1.radius)