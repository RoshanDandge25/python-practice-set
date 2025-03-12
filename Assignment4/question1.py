# 1. Write a Python program that finds the longest word in a list of strings. Use
# map() to calculate the length of each word, and filter() to get the word with the
# maximum length.

# words = ["python", "functional", "programming", "is", "powerful"]



name_list = []
size = int(input("HOW MANY NAMES YOU WANT ENTER = "))
for names in range(size):
    names = input("ENTER THE NAMES : ")
    name_list.append(names)

print(f"YOU ENTERD LIST IS = {name_list}")

# Use map() to calculate the length of each word
word_lengths = list(map(len, name_list))

# Find the maximum length
max_length = max(word_lengths)

# Use filter() to get the longest word(s)
longest_words = list(filter(lambda word: len(word) == max_length, name_list))

# Print the result
print(f"Longest word is = {longest_words}")
