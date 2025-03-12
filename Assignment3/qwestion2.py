# 2) Write a program that accepts a list from user and print the alternate element
# of list.

userinput=[]
numbers=int(input("Enters the size of list: "))
for num in range (numbers):
    userinput.append(input("Enters the numbers :" ))

print(f"Alternative elements {userinput[::2]} ")

