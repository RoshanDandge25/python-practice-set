# 6) Write a program in Python to find out the frequency of each number in
# stored in a list using a python dictionary.
# Example
# List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]
# Output ={1: 1, 2: 3, 3: 1, 4: 3, 5: 2, 6: 3, 7: 2, 8: 1, 9: 1, 23: 1}

def function():
    num_list= [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]

    num_count={}
    for num in num_list:
        if num in num_count:
            num_count[num]+=1
        else:
            num_count[num]=1

    # for nums , count in num_count.items():

    print(f"output = {num_count}")

function()
