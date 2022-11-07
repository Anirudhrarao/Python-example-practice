def fact_num(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        fact = 1
        while num:
            fact *= num
            num -= 1
        return fact
print(fact_num(5))