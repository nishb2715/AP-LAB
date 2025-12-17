#Implement encryption and decryption using Caesar Cipher.
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
if mode in ['encrypt', 'decrypt']:
    transformed_text = caesar_cipher(text, shift, mode)
    print(f"The {mode}ed text is: {transformed_text}")
else:
    print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
    