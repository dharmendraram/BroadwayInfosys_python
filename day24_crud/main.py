from create import create_student
from read import read_student
from update import update_student
from delete import delete_student


def run_crud():

    choice = input("Enter your choice (c/r/u/d/e):")

    def exit_from_crud():
        print("Thank You. See you again")

    if choice.lower() == "c":
        contiunee = create_student()
        run_crud() if contiunee else exit_from_crud()
    elif choice.lower() == "r":
        read_student()
    elif choice.lower() == "u":
        update_student()
    elif choice.lower() == "d":
        delete_student()
    else:
        exit_from_crud()


if __name__ == "__main__":
    run_crud()