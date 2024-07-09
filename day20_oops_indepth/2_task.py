"""
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. 
Implement subclasses for different shapes like circle, triangle, and square.
"""
import math


class Shape:
    def __init__(self,lenght):
        self.lenght = lenght

class Circle(Shape):

    
    def area_of_circle(self):
        return math.pi * self.lenght**2
    
    def peremeter_of_circle(self):
        return 2 * math.pi * self.lenght

class Triangel(Shape):
   
    
    def area_of_triangle(self):
        return math.sqrt(3) / 4 * self.lenght ** 2
    
    def peremeter_of_triangle(self):
        return 3 * self.lenght

class Square(Shape):
    
        
    def area_of_square(self):
        return self.lenght**2
    
    def peremeter_of_square(self):
        return 4 * self.lenght

num = float(input("Enter the value of number :"))
circle = Circle(num)
print(f"Area of circle is {circle.area_of_circle()}")
print(f"Peremetr of circle is {circle.peremeter_of_circle()}")

triangel = Triangel(num)
print(f"Area of circle is {triangel.area_of_triangle()}")
print(f"Peremetr of circle is {triangel.peremeter_of_triangle()}")

square = Square(num)
print(f"Area of circle is {square.area_of_square()}")
print(f"Peremetr of circle is {square.peremeter_of_square()}")

