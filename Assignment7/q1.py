# Create a class "Employee" with an instance variable 'name' and 
# a class variable 'company' (set to "Google"). Display both.

class Employee:
    company = "Google"
    def __init__(self , name):
        self.name = name
        def display():
            print(self.name , Employee.company)

emp=Employee("Roshan")
print(emp.name)
print(emp.display())

        