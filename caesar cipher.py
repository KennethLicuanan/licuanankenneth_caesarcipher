def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

texts = ["KENENTH LICUANAN", "IT36A", "BSIT", "Aim To Excel"]
shifts = [3, 3, 3, 3]

for text, shift in zip(texts, shifts):
    encrypted_text = caesar_cipher_encrypt(text, shift)
    print("Original text:", text)
    print("Encrypted text:", encrypted_text)

    decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
    print("Decrypted text:", decrypted_text)
    print()