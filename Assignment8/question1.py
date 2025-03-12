# 1. Write a function in Python to count and display the total number of words in
# a text file


def function():
    file = open("./asseightquesone.txt", "rt")  
    content = file.read()
    lines = content.split('\n')
    # print(f"content {content}")
    word=content.split()
    print('-'*50)
    print(f"total number of words = {len(word)}")
    print('-'*50)
    file.close()
function()
