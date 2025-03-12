# 4) Write a program to find index of element ‘e’ in given


vowels=['a','e','i','o','u']
# print(f"index of e is = {vowels.index("e")}")


for index in range(len(vowels)):
    if vowels[index]=="e":
        print(f"index of e is {index}")