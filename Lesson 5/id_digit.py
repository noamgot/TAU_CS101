def control_digit(ID):
    s = 0
    for i in range(8):
        digit = int(ID[i])
        if i%2 == 0: #i is one of 0,2,4,6
            s = s+digit
        else: #i is one of 1,3,5,7
            digit = digit * 2
            if digit <= 9:
                s = s+digit
            else:
                ones = digit%10
                tens = 1 #digit is either 10, 12, 14, 16, or 18
                s = s + tens + ones

    ones = s%10
    check_digit = 10 - ones

##    if check_digit == 10:
##        check_digit = 0

    return check_digit