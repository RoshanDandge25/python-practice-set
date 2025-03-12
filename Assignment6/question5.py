# 5. Design a system where a University manages multiple Departments, and each
# Department has multiple Professors.

# Functionalities:
# 1. Add a Department to the university.
# 2. Recruit Professors into specific departments.
# 3. Display University Details, including departments and professors.
# 4. Exit the system when done.

# Fields for Each Class:
# 1. University Class
# name (string): University name
# location (string): University location
# departments (list): Stores all departments
# 2. Department Class
# name (string): Department name
# professors (list): Stores all professors in the department
# 3. Professor Class
# id (int): Unique ID for each professor
# name (string): Professor's name
# specialization (string): Subject the professor specializes in



class Professor:
    def __init__(self, professor_id, name, specialization):
        self.id = professor_id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Specialization: {self.specialization}"


class Department:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professor(self, professor):
        self.professors.append(professor)

    def __str__(self):
        professors_list = "\n\t".join(str(prof) for prof in self.professors)
        return f"Department: {self.name}\nProfessors:\n\t{professors_list if self.professors else 'None'}"


class University:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def display_details(self):
        print(f"University: {self.name}, Location: {self.location}")
        if self.departments:
            for department in self.departments:
                print(department)
        else:
            print("No departments available.")

# User Interaction
def main():
    university_name = input("Enter University Name: ")
    university_location = input("Enter University Location: ")

    university = University(university_name, university_location)

    while True:
        print("\nMenu:")
        print("1. Add a Department")
        print("2. Recruit a Professor")
        print("3. Display University Details")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            department_name = input("Enter Department Name: ")
            university.add_department(Department(department_name))
            print(f"Department '{department_name}' added.")
        elif choice == '2':
            if not university.departments:
                print("No departments available. Add a department first.")
                continue
            print("Available Departments:")
            for i, department in enumerate(university.departments):
                print(f"{i + 1}. {department.name}")
            dept_choice = int(input("Select a department by number: ")) - 1
            if 0 <= dept_choice < len(university.departments):
                professor_id = int(input("Enter Professor ID: "))
                professor_name = input("Enter Professor Name: ")
                professor_specialization = input("Enter Professor Specialization: ")
                professor = Professor(professor_id, professor_name, professor_specialization)
                university.departments[dept_choice].add_professor(professor)
                print(f"Professor '{professor_name}' added to department '{university.departments[dept_choice].name}'.")
            else:
                print("Invalid department choice.")
        elif choice == '3':
            university.display_details()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
