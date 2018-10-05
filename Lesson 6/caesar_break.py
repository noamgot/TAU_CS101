def caesar_encrypt(plaintext, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_position = (position + offset) % 26
            new_char = alphabet[new_position]
            # print(char, "-->", new_char)
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
            # print(char, "unchanged")

    return ciphertext


def caesar_decrypt(ciphertext, offset):
    plaintext = caesar_encrypt(ciphertext, -offset)
    return plaintext


ciphertext = "iwxh xh iwt dgxvxcpa eapxcitmi"


def caesar_break(ciphertext):
    for offset in range(1, 26):
        maybe = caesar_decrypt(ciphertext, offset)
        print(offset, "-->", maybe)


# caesar_break(ciphertext)
caesar_break("ps")
