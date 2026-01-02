#Build a Caesar Cipher
def caesar(text,shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[0:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper() , shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)
    

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)

#will finish later
