# 3)write a program to find given number is positive ,nigetive or zero

number=int(input("ENTER THE NUMBER : "))

if number>0:
    print(f"{number} is Positive ")
elif number<0:
    print(f"{number} is Negative")
elif number==0:
    print(f"{number} is Equal to zero")
else:
    print("invalid input")