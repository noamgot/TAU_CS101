def string_to_list(string):
    digits = []
    for ch in string:
        digits += [int(ch)]
    return digits


def control_digit(ID):
    digits = string_to_list(ID)
    for i in range(8):
        if i % 2 == 1:
            temp = digits[i] * 2
            if temp < 10:
                digits[i] = temp
            else:
                digits[i] = 1 + (temp % 10)

    total = sum(digits)
    if total % 10 == 0:
        check_digit = 0
    else:
        check_digit = 10 - (total % 10)
    return str(check_digit)


print(control_digit("12345678"))