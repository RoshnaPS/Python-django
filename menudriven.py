class Student:
    def __init__(self, reg_number, name, marks):
        self.reg_number = reg_number
        self.name = name
        self.marks = marks
        self.result = "Pass" if marks > 35 else "Fail"

    def display_details(self):
        print(f"Register Number: {self.reg_number}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Result: {self.result}")
        print()


def upload_details(students):
    try:
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            reg_number = input("Enter Register Number: ")
            name = input("Enter Name: ")
            marks = int(input("Enter Marks out of 100: "))
            if 0 <= marks <= 100:
                students.append(Student(reg_number,name,marks))
            else:
                print("Marks should be between 0 and 100. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def display_result(students):
    choice = int(input("Select result type:\n1. Pass\n2. Fail\n3. All\n"))
    if choice == 1:
        pass_students = [student for student in students if student.result == "Pass"]
        print("\nPassing Students:")
        for student in pass_students:
            student.display_details()
    elif choice == 2:
        fail_students = [student for student in students if student.result == "Fail"]
        print("\nFailing Students:")
        for student in fail_students:
            student.display_details()
    elif choice == 3:
        print("\nAll Students:")
        for student in students:
            student.display_details()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


def search_student(students):
    choice = int(input("Select search type:\n1. Register Number\n2. Name\n"))
    try:
        if choice == 1:
            reg_number = input("Enter Register Number to search: ")
            student = next((s for s in students if s.reg_number == reg_number), None)
        elif choice == 2:
            name = input("Enter Name to search: ")
            student = next((s for s in students if s.name.lower() == name.lower()), None)
        else:
            print("Invalid choice. Please select 1 or 2.")
            return

        if student:
            print("\nStudent Details:")
            student.display_details()
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid input. Please enter a valid value.")


def main():
    students = []
    while True:
        print("\nMenu:")
        print("1. Upload Details")
        print("2. Result")
        print("3. Search")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                upload_details(students)
            elif choice == 2:
                display_result(students)
            elif choice == 3:
                search_student(students)
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    main()
