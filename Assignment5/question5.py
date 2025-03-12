# 5) In cryptography, a Caesar cipher is a very simple encryption techniques in
# which each letter in the plain text is replaced by a letter some fixed number of
# positions down the alphabet. For example, with a shift of 3, A would be
# replaced by D, B would become E, and so on. The method is named after Julius
# Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13
# places") is a widely used example of a Caesar cipher where the shift is 13. In
# Python, the key for ROT-13 may be represented by means of the following
# dictionary:
# key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x',
# 'l':'y', 'm':'z', 'n':'a',
# 'o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m',
# 'A':'N', 'B':'O', 'C':'P',
# 'D':'Q', 'E':'R','F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A','O':'B',
# 'P':'C',
# 'Q':'D','R':'E', 'S':'F', 'T':'G','U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
# Your task in this exercise is to implement an encoder/decoder of ROT-13. Once
# you're done, You will be able to read the following secret message:
#
# Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
# Note that since English has 26 characters, your ROT-13 program will be able to
# both encode
# And decode texts written in English.


key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 
'l':'y', 'm':'z', 'n':'a', 
'o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 
'A':'N', 'B':'O', 'C':'P', 
'D':'Q', 'E':'R','F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A','O':'B', 
'P':'C', 
'Q':'D','R':'E', 'S':'F', 'T':'G','U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'} 



def rot13_map(text):
    def shift(char):
        if 'A' <= char <= 'Z':  # Uppercase letters
            return chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        elif 'a' <= char <= 'z':  # Lowercase letters
            return chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        return char  # Return unchanged if not a letter

    # Use map() to apply the shift function to each character
    return ''.join(map(shift, text))

# Test cases

secret_message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"


decoded_message = rot13_map(secret_message)
encoded_message = rot13_map(decoded_message)  # Applying ROT-13 again should return original
print('-'*100)

print("Decoded Message:", decoded_message)
print("Re-encoded Message:", encoded_message)

print('-'*100)
