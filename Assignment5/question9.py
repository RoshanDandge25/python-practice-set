# 9) Write a version of a palindrome recognizer that also accepts phrase
# palindromes such as "Go hanga salami I'm a lasagna hog.",
# "Was it a rat I saw?",
# "Step on no pets",
# "Sit on a potato pan, Otis",
# "Lisa Bonet ate no basil",
# "Satan, oscillate my metallic sonatas",
# "I roamed under it as a tired nude Maori",
# "Rise to vote sir", or the exclamation "Dammit, I'm mad!".
# Note that punctuation, capitalization, and spacing are usually ignored.

def is_palindrome_filter_map(phrase):
    
    cleaned_phrase = ''.join(map(str.lower, filter(str.isalnum, phrase)))
    
   
    return cleaned_phrase == cleaned_phrase[::-1]


phrases = [
    "Go hanga salami I'm a lasagna hog.",
    "Was it a rat I saw?",
    "Step on no pets",
    "Sit on a potato pan, Otis",
    "Lisa Bonet ate no basil",
    "Satan, oscillate my metallic sonatas",
    "I roamed under it as a tired nude Maori",
    "Rise to vote sir",
    "Dammit, I'm mad!"
]

for phrase in phrases:
    print(f'\"{phrase}\" -> {is_palindrome_filter_map(phrase)}')
