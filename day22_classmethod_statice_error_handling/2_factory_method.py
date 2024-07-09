import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def get_age_from_year(cls,name,year):
        # current_year =2024
        # age = current_year - year
        age =datetime.datetime.now().year  - year
        return cls(name,age)
        
  
p1 = Person("Alex", 24)
print(p1.age)  # 24

birth_date = 1992
p2 = Person.get_age_from_year("Jone",birth_date)
print(p2.age)  # 32