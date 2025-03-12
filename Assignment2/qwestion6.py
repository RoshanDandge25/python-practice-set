# 6) The marks obtained by a student in 3 different subjects are input by the user. Your program should
# calc ulate the average of subjects and display the grade. The student gets a grade as per the following
# rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

python=int(input("ENTER PYTHON MARKS : "))
java=int(input("ENTER JAVA MARKS : "))
react=int(input("ENTER REACT MARKS : "))

average=(python+java+react)/3
print(f"Average : {average}")

if average > 90 and average<100:
    print("grade A")
elif (average>80 and average<89):
    print("grade B")
elif (average>70 and average<79):
    print("grade C")
elif (average > 60 and average<69):
    print("grade D")
elif (average >0 and average<59):
    print("grade F")
else:
    print("something went wrong")