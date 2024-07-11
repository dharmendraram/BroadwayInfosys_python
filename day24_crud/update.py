import json
filename = "students.json"

def update_student():
    id = input("Enter the student id:")
    key = input("Enter the info you want to update : ")
    value = input(f"Enter the new {key}")

    if key not in ["name","age","address"]:
        print("Info not Avaliable")
    else:
        with open(filename, "r+") as fp:
            students = json.loads(fp.read())
            student = list(filter(lambda s:s["id"] == id ,students))
            if student:
                student=student[0]
                index_of_student = students.index(student)
                student[key] = value
                students[index_of_student] = student
                fp.seek(0)
                fp.write(json.dumps(students, indent=2))
                print("Student update successfully...")
            else:
                print("Information is not available")

    choice = input("Do you want to continue? (y/n) ")
    return True if choice.lower() == "y" else False