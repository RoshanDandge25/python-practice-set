# 6) Find and display the largest number of a list without using built-in function
# max(). Your program should ask the user to input values in list from keyboard.




def max_num_list():
    num_list=[]
    size=int(input("ENTER THE SIZE OF LIST = "))
    for num in range (size):
        num=int(input("ENTER THE NUMBERS : "))
        num_list.append(num)
    print(f"YOU ENTERD LIST IS = {num_list} ")
    
    large_num= num_list[0]
    for num in num_list:
        if num>large_num:
            large_num = num
    print(f"largest num in above list is = {large_num}")

max_num_list()