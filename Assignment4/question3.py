# 3. Write a Python program to convert a given list of integers and a tuple of
# integers into a list of strings. Use Python map.

num_list = [1, 2, 3, 4, 5]
num_tuple = (6, 7, 8, 9, 10)


str_list = list(map(str, num_list))
str_tuple = list(map(str, num_tuple))


print("List of strings:", str_list)
print("Tuple of strings:", str_tuple)
