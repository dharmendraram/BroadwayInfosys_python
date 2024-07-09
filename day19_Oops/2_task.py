"""
Create a class Person with instance attributes name and age. 
add a  class attribute nationality
Create a method get_details in this class to print name and age.

Create another class Employee with instance attributes salary and 
designation and inherits the Person class. Create a method get_details in this class to 
print name, age, salary and designation of the Employee.

"""

class Person:
    nationality="Nepali"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def get_details(self): # instance method
        return f"Person name is {self.name} and age is {self.age} and my nationality is {self.nationality}"

class Employee(Person):
    def __init__(self, name, age,salary,degin): # instance attributes
        super().__init__(name, age)
        self.salary = salary
        self.degin = degin
        
    def get_details(self): # instance method
        x=super().get_details()
        return f"{x} ,salary is {self.salary} and degination is {self.degin}"
    

emp = Employee("Dharmendra",25,30000,"Front-end Dev")
print(emp.get_details())