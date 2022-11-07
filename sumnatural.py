def sum_natural(num):
    sum = 0
    for i in range(1,num+1):
        sum += (i*i)
    return sum

print(sum_natural(4))