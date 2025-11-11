def encrypt(message,key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char)-base+key) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(message,key):
    return encrypt(message,-key)

choice = input("Do you want to encrypt or decrypt a message?").strip().lower()
if choice == 'e':
    msg = input("Enter the message to encrypt: ")
    k = int(input("Enter the key (shift value): "))
    print("Encrypted message:", encrypt(msg, k))
elif choice == 'd':
    msg = input("Enter the message to decrypt: ")
    k = int(input("Enter the key (shift value): "))
    print("Decrypted message:", decrypt(msg, k))
else:
    print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")