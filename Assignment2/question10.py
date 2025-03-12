#10) write a function to return compound interest.
#CI = P (1 + r/n) ^ nt
#P - Principal Amount
#r - Rate of interest
#n - Number of times interest compounds in a year
#t - Number of years

def CompoundIntrest():
    P = float(input(f"Enter Principal Amount : "))
    R = float(input(f"Rate of Interest : "))/100
    N = int (input(f"Enter Number of times interest compounds in a year : "))
    T = int (input(f"Number of years : "))


    CI = P * (1 + R / N) ** (N * T)
    return CI

result=CompoundIntrest()
print('-'*50)

print(f"compound interest is : {result}")