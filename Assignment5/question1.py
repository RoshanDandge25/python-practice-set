# ) Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name


def function():
    people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod':'Purple', 'Jenny': 'Pink'}

    #A. Find out how many students are in the list

    print(f"A. Find out how many students are in the list = {len(people)}")

    #B. Change Lisa’s favourite colour

    people['Lisa']='orange'
    print(f"B. Change Lisa’s favourite colour = {people}")

    #C. Remove 'Jenny' and her favourite colour

    people.__delitem__('Jenny')
    print(f"C. Remove 'Jenny' and her favourite colour = {people}")

    #D. Sort and print students and their favourite colours alphabetically by name
    sorted(people)
    print(f"D. Sort and print students and their favourite colours alphabetically by name = {people}")


function()
