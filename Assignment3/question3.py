#3) Replace single element ‘b’ in given list [’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3]

def replace_list_to_num():
    num_list=['a','b','c','d','e']
    print(f"list is = {num_list}")

    index=num_list.index('b')

    num_list[index:index+1]=[1,2,3]
    print(f"updated list is = {num_list}")

replace_list_to_num()