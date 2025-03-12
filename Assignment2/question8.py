#8) Write a program that prompts the user to input a character and determine the character is
#vowel or consonant.

char=(input("Engter the character : "))

# result= "aeiou" if char in "vowels" else "consonant"
# print(f"you entered {char} is  {result} ")

    
if char in 'aeiou':
    print(f"you entered is {char} is Vowel")
elif char in 'AEIOU':
    print(f"you entered is {char} is Vowel")
else:
    print(f"you entered is {char} is consonant")