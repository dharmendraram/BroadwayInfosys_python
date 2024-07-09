"""
    Write a Python program to create a calculator class. 
    Include methods for basic arithmetic operations.
    """

class Calculator:
    result =0
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        self.result = self.num1 + self.num2
        return self.result
    
    def sub(self):
        self.result= self.num1 - self.num2
        return self.result
    
    
    def mul(self):
        self.result= self.num1 * self.num2
        return self.result
        
    
    def div(self):
        if self.num2 != 0:
            self.result= self.num1 / self.num2
            return self.result
            
        else:        
            return "Cannot divide by Zero"
        

num1 = float(input("Enter the value of num1: "))
num2 = float(input("Enter the value of num2: ")) 
 
cal = Calculator(num1,num2)

result = cal.add()
print("Addition of two number is :", result)

result = cal.sub()
print("Subtraction of two number is :", result)

result = cal.mul()
print("Multiplication of two number is :", result)

result = cal.div()
print("Division of two number is :", result)
        