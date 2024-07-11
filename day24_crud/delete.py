import json

filename = "students.json"

def delete_student():
    id = input("Enter the student id:")

    with open(filename, "r") as fp:
        students = json.loads(fp.read())  # [{"id": 1}, {"id": 2}, {"id": 3}]
    student = list(filter(lambda s: s["id"] == id, students))  # [{}] or []
    if student:
        student = student[0]
        students.remove(student)
        with open(filename, "w") as fp:
            fp.write(json.dumps(students, indent=2))
        print("Student delete successfully...")

    else:
        print("Information is not available")

    choice = input("Do you want to continue? (y/n) ")
    return True if choice.lower() == "y" else False