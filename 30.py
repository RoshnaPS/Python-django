def student(roll_no):
    try:
        with open("new.txt", "r") as file:
            for line in file:
                stu_data = line.strip().split(',')
                if stu_data[0] == roll_no:
                    return f"Roll Number: {stu_data[0]}\nName: {stu_data[1]}\nCourse: {stu_data[2]}"
        return "Student not found."
    except FileNotFoundError:
        return "File not found. Please make sure 'stud.txt' exists."

r= input("Enter the Roll Number to search: ")
result = student(r)
print(result)