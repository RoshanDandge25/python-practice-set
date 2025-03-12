# 8) Write a function translate() that will translate a text into "rövarspråket"
#  (Swedish for "robber's language"). That is, double every consonant and place
# an
#  occurrence of "o" in between. For example, translate("this is fun") should
# return
#  the string "tothohisos isos fofunon".

def translate(text):
    vowels='aeiouAEIOU'
    result=''

    for char in text:
        if char.isalpha() and char not in vowels:
            result+=char+"o"+char

        else:
            result+=char
    return result


print(f"THE OUTPUT IS = " ,translate("this is fun"))
