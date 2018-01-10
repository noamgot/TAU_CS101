from random import randint
from time import time


def generate_random_list(n):
    return [randint(0, 999999) for i in range(n)]


lst = generate_random_list(100000)
start = time()
sortedLst = sorted(lst)
end = time()
print("Time measured for Python's sorted function: " + str(round(end - start, 3)) + " seconds")
