# 3. Create a class 'Student' with rollno, studentName, course ,dictionary of
# marks(subjectName -marks [5]).
# Provide following functionalities
# A. initializer
# B. override __str__ method
# C. accept student data
# D. Print student data
# E. accept records of 5 students and Print it


   
class Student:
    def __init__(self, rollno, studentName, course, marks):
        self.rollno = rollno
        self.studentName = studentName.title()
        self.course = course.title()
        self.marks = marks
    
    def accept_std_data(self):
        self.rollno = input("Enter roll number: ")
        self.studentName = input("Enter Name: ").title()
        self.course = input("Enter your course: ").title()
        
        self.marks = {}
        num_subjects = int(input("Enter number of subjects: "))
        
        for num in range(num_subjects):
            subject = input(f"Enter subject name {num+1}: ").title()
            
            while True:
                try:
                    mark = int(input(f"Enter marks for {subject}: "))
                    if mark < 0 or mark > 100:
                        print("Marks should be between 0 and 100.")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid integer.")

            self.marks[subject] = mark
    
    def print_std_data(self):
        print("\n======================")
        print(f"Roll Number: {self.rollno}")
        print(f"Name: {self.studentName}")
        print(f"Course: {self.course}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print("======================")

students = []
num_students = int(input("Enter number of students: "))

for _ in range(num_students):
    student = Student("", "", "", {})  # Create an empty student object
    student.accept_std_data()  # Fill the details using instance method
    students.append(student)

print("\nStudent Records:")
for student in students:
    student.print_std_data()
