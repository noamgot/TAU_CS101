# modify the function as explained:
# 1. The function should print every item it reaches
# 2. If x is in the list, the function should print "x was found in the list"
#    Otherwise, the function should print "x is not in the list"
#    (x should be the number we're looking for, e.g 7, 2, etc.)

def search_print(L, x):
    for e in L:
        if e == x:
            return True
    # if we got here the search failed
    return False
