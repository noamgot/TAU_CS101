def char_count(text):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        how_many = text.count(char)
        if how_many > 0:
            percent = how_many * 100 / len(text)
            print(char, "frequency:", percent, "%")

char_count("aaab")