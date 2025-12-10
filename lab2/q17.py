#Implement encryption and decryption using Caesar Cipher.
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
if mode == 'encrypt':
    encrypted_text = caesar_cipher(text, shift, mode='encrypt')
    print(f"Encrypted text: {encrypted_text}")
elif mode == 'decrypt':
    decrypted_text = caesar_cipher(text, shift, mode='decrypt')
    print(f"Decrypted text: {decrypted_text}")
else:
    print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")

    