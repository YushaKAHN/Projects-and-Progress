import random
import string

chars = " "+string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)
# print(f"chars:{chars}")
# print(f":{key}")

# encrypt
plain_text = input("Enter your message to encrypt it :")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message:{plain_text}")
print(f"Encrypted message:{cipher_text}")


# Decrypt

cipher_text = input("Enter your message to decrypt it :")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text = chars[index]

print(f"Encrypted message:{cipher_text}")
print(f"Original message:{plain_text}")
