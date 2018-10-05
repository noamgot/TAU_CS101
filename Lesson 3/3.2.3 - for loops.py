def my_max(lst):
    maximum = lst[0]
    for x in lst:
        if x > maximum:
            maximum = x
    return maximum

# bad version:
def my_max(lst):
    maximum = lst[0]
    for x in lst:
        if x > maximum:
            maximum = x
        return maximum