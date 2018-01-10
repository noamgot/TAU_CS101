# # modify the function as explained:
# # Instead of returning True or False, the function should count the number
# # of comparisons it made (i.e how many times it checked if a number from
# # the list L equals to x) and return that number
#
# def search_cnt(L, x):
#     for e in L:
#         if e == x:
#             return True # <-- change!
#     # if we got here the search failed
#     return False # <-- change!

def search_cnt(L, x):
    cnt = 0
    for e in L:
        cnt += 1
        if e == x:
            break
    return cnt