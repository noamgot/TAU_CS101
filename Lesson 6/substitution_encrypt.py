def sub_encrypt(plaintext, alphabet, shuffled):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_char = shuffled[position]
            print(char, "-->", new_char)
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
            print(char, "unchanged")

    return ciphertext


alphabet = "abcdefghijklmnopqrstuvwxyz"
shuffled = "psfvinytdugqrjhwebmkzoxcla"

# print(sub_encrypt("hello world", alphabet, shuffled))
print(sub_encrypt("hello world!", alphabet, shuffled))