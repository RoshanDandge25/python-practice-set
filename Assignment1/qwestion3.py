#3)write a program to find given number is positive ,nigetive or zero.

num1=int(input(f"Enter the number : "))


def face_val(param):
    digit4 = (param // 1000) % 10
    digit3 = (param // 100) % 10
    digit2 = (param // 10) % 10
    digit1 = param % 10
    
    return "{}  {}  {}  {}".format(digit4, digit3, digit2, digit1)

res = face_val(num1)
print(f"a. the face value is : {res}")

def place_val(param):
    digit1 = param % 10               
    digit2 = (param // 10) % 10 * 10
    digit3 = (param // 100) % 10 * 100
    digit4 = (param // 1000) % 10 * 1000

    return "{}  {}  {}  {}".format(digit1, digit2, digit3, digit4)

res = place_val(num1)
print(f"b. the place value is : {res}")

def rev_val(param):
    digit1 = param % 10        
    digit2 = (param // 10) % 10   
    digit3 = (param // 100) % 10   
    digit4 = (param // 1000) % 10       

    return "{}  {}  {}  {}".format(digit1, digit2, digit3, digit4)

res_reverse = rev_val(num1)
print(f"c. The number in reverse order by changing place values is : {res_reverse}")