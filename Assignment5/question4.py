# 4) In following text count occurrence of each letter (irrespective of case). Hint:
# convert string to same case e.g. text.lower(). Do not use Counter collection.
# text = """Python is a high-level, general-purpose programming language. Its
# design philosophy emphasizes code readability with the use of significant
# indentation. Python is dynamically typed and garbage-collected. It supports
# multiple programming paradigms, including structured, object-oriented and
# functional programming."""

def function():
    text= """Python is a High-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant
    indentation. Python is dynamically typed and garbage-collected. It supports
    multiple programming paradigms, including structured, object-oriented and
    functional programming."""

    print(f"in lowercase = {text.lower()}")


    letter_count={}
    for ch in text:
        if ch.isalpha():
         if ch in letter_count:
            letter_count[ch]+=1
         else:
            letter_count[ch]=1

         sorted_order=sorted(letter_count.items())

    for character , count in sorted(letter_count.items()):

        print(f" character is = {character} and count is = {count}")
function()

