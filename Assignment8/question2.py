# 2. Write a function in python to count the number of lines from a text file
# "story.txt" which is not starting with an alphabet "C".
# Example: If the file "test.txt" contains the following lines:
#  Connecting DB’s with Python.
#  Working with DB’s using Python.
#  Accessing and Manipulating DB’s.
#  Creation of Python virtual Environment.
#  Working with beautiful soup.
#  Working with matplotlib, seaborn.
# The function should display the output as 4

def numlinecount():
    file=open("./story.txt" ,"rt")
    lines=file.readlines()

    file.close()
    
    count=0
    
    for line in lines:
        line = line.strip()  
        if line and not line.startswith("C"):
            count+=1
    print('-'*50)       
    print(f"Total lines NOT starting with 'C': {(count)}")   
    print('-'*50)  

numlinecount()