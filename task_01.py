def caesar_cipher(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

# User input
text = input("Enter text: ")
shift = int(input("Enter shift value: "))

# Encrypting the text
encrypted_text = caesar_cipher(text, shift)


# Decrypting the text
decrypted_text = caesar_cipher(encrypted_text, -shift)

#print the decrypted message
print(f"Decrypted Text: {decrypted_text}")

#print the ecrypted message
print(f"Encrypted Text: {encrypted_text}")