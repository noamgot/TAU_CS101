import random

def count_rolls_until_6():
    res = random.choice([1, 2, 3, 4, 5, 6])
    print(res)
    count_rolls = 1
    while res != 6:
        res = random.choice([1, 2, 3, 4, 5, 6])
        print(res)
        count_rolls = count_rolls + 1

    return count_rolls


rolls = count_rolls_until_6()
print(rolls, "rolls were needed to get 6 in a fair dice experiment")