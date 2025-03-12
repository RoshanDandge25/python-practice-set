class Employee:
    company = "Google"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

    def display(self):
        print(self.name, Employee.company)  # Prints name and company

# Creating an object
emp = Employee("Roshan")

# Printing instance variable
print(emp.name)

# Correct way to call the method (without print())
emp.display()
