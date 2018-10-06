def max2(a, b):
    if a > b:
        return a
    else:
        return b

def max3_v3(a,b,c):
    max_a_b = max2(a,b)
    max_all = max2(max_a_b, c)
    return max_all

result = max3_v3(1,2,3)