def max3_v1(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

a = 1
b = 2
c = 3
result = max3_v1(a,b,c)