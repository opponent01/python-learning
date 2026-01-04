#Build a Caesar Cipher
def caesar(text,shift,encrypt=True):
    if  not isinstance(shift,int):
        return "Shift must be an integer value."
    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."
    if not encrypt:
        shift = -shift

    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[0:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper() , shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)
    
def encrypt(text,shift):
    return caesar(text,shift)

def decrypt(text,shift):
    return caesar(text,shift,encrypt=False)

encrypted_text = encrypt("hello",10)
decrypted_text = decrypt("rovvy",10)
print("enrypted text:",encrypted_text)
print("decrypted text:",decrypted_text)

