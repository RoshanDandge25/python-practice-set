# 7) Write a program to read 6 numbers and create a dictionary having keys EVEN
# and ODD.
#  Dictionary's value should be stored in list. Your dictionary should be like:
#  {'EVEN':[8,10,64], 'ODD':[1,5,9]}


def function():
    num_list=[]
    even=[]
    odd=[]
    for num in range(6):
        num= int(input("enter  ingteger numbers ="))
        num_list.append(num)

    print(f"you entered list is = {num_list}")

    for numm in num_list:
        if numm%2==0:
            even.append(numm)

        else:
            odd.append(numm)

    print(f"EVEN LIST = {even}")
    print(f"ODD LIST  = {odd}")


function()


