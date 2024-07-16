import csv

filename = "students.csv"

with open(filename, "r") as cr:
    data = csv.DictReader(cr)
    result=[]
    for each in data:
        result.append(each)
print(result)
