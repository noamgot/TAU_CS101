from random import randint
from time import time

def generate_random_list(n):
    return [randint(0,999999) for i in range(n)]

def SelectionSort(L):
    ''' return a sorted copy of lst '''
    n = len(L)
    sortedL = []
    for i in range(n):
        minimum = min(L)
        L.remove(minimum)
        sortedL.append(minimum)
    return sortedL

lst = generate_random_list(100000)
start = time()
sortedLst = SelectionSort(lst)
end = time()
print("Time measured for SelectionSort: " + str(round(end-start,3)) + " seconds")