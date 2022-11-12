def sum_digit(ls):
    res = []
    for i in ls:
        sum = 0
        for digit in str(i):
            sum += int(digit)
        res.append(sum)
    return res
print(sum_digit([12,34]))