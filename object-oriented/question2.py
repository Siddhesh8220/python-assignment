# 2] Create a base class
# Shapes. It must have 2 suitable instance variables and 2 suitable methods.

# Create 2 child class of
# Shapes. For example Triangle and Quadrilateral. They must inherit the Shapes class and override 1 variable and 1 method. They must have 1 additional attribute and
# method.

# Create 1 child class each of
# the above Triangle & Quadrilateral. They must override 1 method and have 2 additional attributes and 1 additional method.

# Your program must
# instantiate the lowest child classes and print all attributes and methods of the class and all inherited attributes and methods as well. Suitable error handling must be done for
# all methods.

import math

class Shapes:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides


    def info(self):
        return self.name + " " + str(self.sides)
    
    
    def getsides(self):
        return self.sides

class Triangle(Shapes):
    def __init__(self, name, base, height):
        super().__init__(name, 3)
        self.base = base
        self.height = height

    def info(self):
        return self.name + " " + str(self.sides) + " " + str(self.base) + " " + str(self.height)
    
    def area(self):
        return self.base * self.height / 2

class Quadrilateral(Shapes):
    def __init__(self, name, sides, a, b, c, d):
        super().__init__(name, sides)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def info(self):
        return self.name + " " + str(self.sides) + " " + str(self.a) + " " + str(self.b) + " " + str(self.c) + " " + str(self.d)
    
    def perimeter(self):
        return self.a + self.b + self.c + self.d


class Rectangle(Quadrilateral):
    def __init__(self, name, sides, a, b):
        super().__init__(name, sides, a, b, a, b)
    
    def info(self):
        return "Rectangle:" +self.name +", side-one:" + str(self.a) + ", side-two:" + str(self.b) 
    
    
class EquilateralTriangle(Triangle):
    def __init__(self, name, side):
        super().__init__(name, side,side,side, side, math.sqrt(3) * side / 2)
    
    def info(self):
        return "Equilateral:"+self.name + " length:" + str(self.sides)  + " Base:" + str(self.base) + " Height:" + str(self.height)
    
   
    
rect = Rectangle("Rectangle one", 4, 4, 3)
print(f"Info: {rect.info()}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Side lenghts: {rect.a, rect.b, rect.c, rect.d}")
print(f"No of sides: {rect.sides}")