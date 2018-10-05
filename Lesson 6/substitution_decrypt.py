def sub_encrypt(plaintext, alphabet, shuffled):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_char = shuffled[position]
            # print(char, "-->", new_char)
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
            # print(char, "unchanged")

    return ciphertext


def sub_decrypt(ciphertext, alphabet, shuffled):
    plaintext = sub_encrypt(ciphertext, shuffled, alphabet)
    return plaintext


alphabet = "abcdefghijklmnopqrstuvwxyz"
shuffled = "psfvinytdugqrjhwebmkzoxcla"

ciphertext = sub_encrypt("hello world", alphabet, shuffled)
print("ciphertext:", ciphertext)
plaintext = sub_decrypt(ciphertext, alphabet, shuffled)
print("plaintext:", plaintext)
