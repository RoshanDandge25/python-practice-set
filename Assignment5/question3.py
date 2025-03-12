# 3) Define a function subtract() that takes two lists and returns difference (i.e.
# excess elements from list1). If list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60],
# then result should be [10, 20].


def subtract(list1 ,list2):
    print(f" orignal list are list 1 = {list1}")
    print(f" orignal list are list 2 = {list2}")

    result =list(set(list1) -set(list2))
    print(f"The diff of list (list1-list2) = {result}")



list1 =[10, 20, 30, 40]
list2 =[30, 40, 50, 60]



subtract(list1 , list2)