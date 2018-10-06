def max2(a, b):
    if a > b:
        return a
    else:
        return b

def max3_v3(a,b,c):
    max_a_b = max2(a,b)
    max_all = max2(max_a_b, c)
    return max_all

def max10(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    x = max3_v3(a1, a2, a3)
    y = max3_v3(a4, a5, a6)
    z = max3_v3(a7, a8, a9)
    max_xyz = max3_v3(x, y, z)
    result = max2(max_xyz, a10)
    return result

res = max10(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)