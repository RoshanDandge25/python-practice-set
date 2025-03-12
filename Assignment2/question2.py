#2)Write a Python function to find the maximum of three numbers.
#from question10 import result


def MaximumNum():
    num1=int(input(f"Enter 1st Value : "))
    num2=int(input(f"Enter 2nd Value : "))
    num3=int(input(f"Enter 3rd value : "))
    result = max(num1, num2, num3)
    return result



maxvalue=MaximumNum()
print(f"Maximum Num Is : {maxvalue}")