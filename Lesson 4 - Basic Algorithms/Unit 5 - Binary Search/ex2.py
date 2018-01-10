def binary_search(L, x):
    ''' search for x in my_list, which MUST BE SORTED !! '''
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == x:
            return True
        else:
            if L[mid] < x:  # go to right half
                left = mid + 1
            else:  # go to left half
                right = mid - 1

    return False  # if we got here the search failed

# Test binary_search with different valuse of x. Do not change anything else!
x = 1
print(binary_search([5,2,8,4,1],x))