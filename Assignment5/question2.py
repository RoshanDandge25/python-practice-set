# 2) Write a program to sum all the values of a dictionary.
# Hint dict1 = {‘key 1’: 200, ‘key 2’: 300}
# Expected output
# Result: 500

def function():

    dict1={'key 1':200 , 'key 2':300}
    print(f"{dict1}")

    result=0
    for sum in dict1.values():
      result+= sum
    print(f"Sum all the values of a dictionary = {result}")


function()

