def cube_sum_natural(num):
    sum = 0
    for i in range(1,num+1):
        sum += pow(i,3)
    return sum
print(cube_sum_natural(7))