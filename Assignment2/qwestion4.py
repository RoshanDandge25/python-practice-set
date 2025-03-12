#4) Write a program that prompts the user to input a year and determine whether the year is a leap
#year or not.
#Leap Years are any year that can be evenly divided by 4. A year that is evenly divisible by 100 is a leap y
#ear only if it is also evenly divisible by 400. Example :
from random import choice



def years():
    should_continue='y'
    while should_continue=='y':
        year=int(input("ENTER THE YEAR : "))
        if(year%4==0 and year%100!=0 )or (year%400==0):
            print(f"{year} is leaf year ")
        else:
            print(f"{year} is not leap year")
        should_continue=input("you want run again y/n : ")

years()