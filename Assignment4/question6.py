# 6. Write a Python program that filters out all strings that have more than 5
# characters from a list of strings using the filter() function.
# Input: words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']
# Output: ['Yellow', 'Purple', 'Orange']

def filter_string():

    words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']

    # Use filter() to get words with more than 5 characters
    filtered_words = list(filter(lambda word: len(word) > 5, words))


    print(f"output = {filtered_words}")


filter_string()
