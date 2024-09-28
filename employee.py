class Employee:
    def __init__(self, emp_id, name, department, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.base_salary = base_salary

    def calculate_salary(self, overtime_hours, overtime_rate):
        overtime_salary = overtime_hours * overtime_rate
        total_salary = self.base_salary + overtime_salary
        return total_salary

    def display_employee_details(self):
        try:
            overtime_hours = float(input("Enter overtime hours: "))
            overtime_rate = float(input("Enter overtime rate per hour: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for overtime hours and rate.")
            return

        total_salary = self.calculate_salary(overtime_hours, overtime_rate)
        print("\nEmployee Details:")
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Base Salary: ${self.base_salary}")
        print(f"Overtime Salary: ${overtime_hours * overtime_rate}")
        print(f"Total Salary: ${total_salary}")
employee1 = Employee(10, "Anju", "CS", 50000)
employee1.display_employee_details()
