# 1) Using for loop, write and run a Python program to find factorial from 0 to 10

def factorial():
    fact=1
    for number in range(1,10):
        fact=(fact*number)
        print(f"Factorail of {number} is : {fact}")
    
factorial()