# main.py
from create import create_student
from read import read_student
from update import update_student
from delete import delete_student
def run_crud():
    choice = input("Enter your choice (c/r/u/d/e): ")

    def exit_from_crud():
        print("Thank you. See you again!")

    if choice.lower() == "c":
        contiunee = create_student()
        run_crud() if contiunee else exit_from_crud()
    elif choice.lower() == "r":
        read_more = read_student()
        run_crud() if read_more else exit_from_crud()
    elif choice.lower() == "u":
        udate_more = update_student()
        run_crud() if udate_more else exit_from_crud()
    elif choice.lower() == "d":
        delete_more = delete_student()
        run_crud() if delete_more else exit_from_crud()
    else:
        exit_from_crud()

if __name__ == "__main__":
    run_crud()
