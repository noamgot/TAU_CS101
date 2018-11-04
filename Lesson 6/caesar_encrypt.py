def caesar_encrypt(plaintext, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_position = (position + offset) % 26
            new_char = alphabet[new_position]
            #print(char, "-->", new_char)
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
            #print(char, "unchanged")
    return ciphertext


# print(caesar_encrypt("abc", 1))
# print(caesar_encrypt("xyz", 1))
# print(caesar_encrypt("hello", 10))
# print(caesar_encrypt("Hello!!", 10))
# print(caesar_encrypt("Hello!!", 36))
print(caesar_encrypt("Hello!!", -1))


def caesar_decrypt(ciphertext, offset):
    plaintext = caesar_encrypt(ciphertext, -offset)
    return plaintext

def caesar_break(ciphertext):
    for offset in range(1,26): #go over all possible offsets
        maybe = caesar_decrypt(ciphertext, offset)
        print(offset, maybe)


common_words = ["The", " the ", " to ", " is ", " a " ," I " , "I ", " no ", " yes "]

# Caesar Cipher - decryption
#what is this quote and who said it?
#try to decrypt (you don't know the offset!...)
quote = 'jxu gkuijyed ev mxujxuh q secfkjuh sqd jxyda yi de cehu ydjuhuijydw jxqd jxu gkuijyed ev mxujxuh q ikrcqhydu sqd imyc'