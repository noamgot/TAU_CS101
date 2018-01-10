# Modify the function so it will print in every iteration the values of left, mid and right
# The printing format is:
# left=<left value>, mid=<mid value>, right=<right value<
# example: if the value of left is 0, the value of mid is 7 and the value of right is 15, print:
# left=0, mid=7, right=15

def binary_search_print(L, x):
    ''' search for x in my_list, which MUST BE SORTED !! '''
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        print("left={}, mid={}, right={}".format(left, mid, right))
        if L[mid] == x:
            return True
        else:
            if L[mid] < x:  # go to right half
                left = mid + 1
            else:  # go to left half
                right = mid - 1

    return False  # if we got here the search failed