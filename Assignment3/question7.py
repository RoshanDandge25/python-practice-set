# 7) Write a function filter_long_words() that takes a list of words and an integer
# len and returns the list of words that are longer than len.

def word_size_check():
    name_list=[]
    size=int(input("HOW MANY NAMES YOU WANT ENTER = "))
    for names in range (size):
        names=input("ENTER THE NAMES : ")
        name_list.append(names)

    print(f"YOU ENTERD LIST IS = {name_list}")

    # big_name=name_list[0]
    #
    # for value in name_list:
    #     if len(value)>len(big_name):
    #         big_name=value
    # print(f"large word is {big_name}")

    max_length=max(map(len,name_list))

    larg_word=list(filter(lambda word:len(word)==max_length,name_list))

    print(f"LARGE WORD IS = {larg_word}")

word_size_check()
