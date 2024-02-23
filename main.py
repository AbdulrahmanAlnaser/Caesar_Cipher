import string
alphabet = list(string.ascii_lowercase)
direction = input("Do you want it to be encrypted or decrypted? ").lower()
text = input("Please enter your message: ")
shift = int(input("Please enter the shift number: "))

def Encrypt(text, shift_amount):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            shifted_index = (alphabet.index(letter) + shift_amount) % 26
            cipher_text += alphabet[shifted_index]
        else:
            cipher_text += letter
    print(cipher_text)
    
def Decrypt(text, shift_amount):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            shifted_index = (alphabet.index(letter) - shift_amount) % 26
            cipher_text += alphabet[shifted_index]
        else:
            cipher_text += letter
    print(cipher_text)

if direction == "encrypted":
    Encrypt(text, shift)
elif direction == "decrypted":
    Decrypt(text, shift)
else:
    print("Your choice is not valid.")
