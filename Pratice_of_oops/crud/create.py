
import json
import os

filename = "students.json"

def create_student():
    id = input("Enter student id:")
    name = input("Enter student name:")
    age = input("Enter student age:")
    address= input("Enter student address:")

    student = {"id":id, "name":name, "age":age, "address":address}
    try:
        if not os.path.exists(filename):
            with open(filename, "w") as fp:
                to_dump = json.dumps([student], indent=2)
                fp.write(to_dump)

        else:
            with open(filename, "r+") as fp:
                students = json.loads(fp.read())
                students.append(student)
                fp.seek(0)
                fp.write(json.dumps(students, indent=2))
            print("Students Added Successfully !")
    except IOError as e:
        print(f"Error:{e}")

    choice = input("Do yo want to continue? (y/n):")
    return True if choice.strip().lower() == "y" else False



