def caesar(text,shift,encrypt=True):
    if not isinstance(shift,int):
        print("shift must be an integer")
    if shift>25 or shift<1:
        print("shift must be between 1 and 25")
    if not encrypt:
        shift = -shift
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper() ,shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)
def encrypt(text,shift):
    return caesar(text,shift)
def decrypt(text,shift,encrypt=False):
    return caesar(text,shift,encrypt)


encrypted_text= encrypt("hello",4)
decrypted_text= decrypt("lipps",4)

print("encrypted text:",encrypted_text)
print("decrypted text:",decrypted_text)
