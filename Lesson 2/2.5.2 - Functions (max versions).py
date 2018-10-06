def max2(a,b):
    if a > b:
        return a
    else:
        return b

# result = max2(3,5)
# print(result)
# result2 = max2(4,-5)
# print(result2)
x = 4
y = -5
#result3 = max2(x,y)
#print(result3)
result4 = max2(x + y + 3, x*y)
#print(result4)

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

result5 = max3_v1(1,2,3)
#print(result5)

def max3_v2(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

result6 = max3_v2(1,2,3)
print(result6)