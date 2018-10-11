def my_max(lst):
    maximum = lst[0]
    for x in lst:
        if x > maximum:
            maximum = x
    return maximum

#print(my_max([3,4,2,5,1]))
#L = [3,4,2,5,1]
L = ["orange", "apple", "banana"]
print(my_max(L))



# bad version of my_max:
def my_bad_max(lst):
    maximum = lst[0]
    for x in lst:
        if x > maximum:
            maximum = x
        # Notice the wrong indentation:
        return maximum