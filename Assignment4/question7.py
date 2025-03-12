#Filtereed greater than 10 numbers from list

def filter_numbers():
    num_list= [5, 12, 3, 18, 9, 20, 22, 21]
    print(f"our list is = {num_list}")
    filternum=list(filter(lambda x:x>10,num_list))
    print(f"Filtereed greater than 10 numbers from list ={filternum}")

filter_numbers()
