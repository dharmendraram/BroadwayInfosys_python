"""
1. Write a Python program to create a class representing a Circle. 
Include methods to calculate its area and perimeter.

"""
import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def calculate_area_of_circle(self):
        area = math.pi * self.radius**2
        return area
    
    def calculate_peremeter_of_circle(self):
        peremeter = 2 * math.pi * self.radius
        return peremeter

radius = float(input("Enter the value of radius: "))

circle = Circle(radius)

area = circle.calculate_area_of_circle()
peremeter = circle.calculate_peremeter_of_circle()

print("Area of the circle is :", round(area,2))
print("Peremeter of the circle is :", round(peremeter,2))
