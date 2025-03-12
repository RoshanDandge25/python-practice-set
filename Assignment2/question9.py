#9) write a function to return simple interest
#To calculate simple interest, you can use the formula: SI = (P × R × T) / 100. In this formula,
#SI: Stands for simple interest
# P: Represents the principal amount
#R: Represents the interest rate per year
#T: Represents the time in years

def SimpleIntrest():

    p=int(input("Enter the principal amount : "))
    r=int(input("Enter Rate of Intrest : "))
    t=int(input("Enter Years : "))

    SI=(p*r*t)/100
    return SI

result=SimpleIntrest()
print('-'*50)
print(f"The Simple Intrest Is : {result}")

SimpleIntrest()
