# program to create a Caesar encryption


def caesar_encrypt(string, key):
    encrypted = ""
    for char in string:
        if char.isalpha():
            
            
            # eee lines manasilayilla
            # ascii_offset = ord('A') if char.isupper() else ord('a')
            # shifted = (ord(char) - ascii_offset + key) % 26 
            # encrypted += chr(shifted + ascii_offset)
        else:
            encrypted += char
    return encrypted

# Example usage
input_string = "Hello, World!"
key = 3
encrypted_string = caesar_encrypt(input_string, key)
print(encrypted_string)  # Output: Khoor, Zruog!
