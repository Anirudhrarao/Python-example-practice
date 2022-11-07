num = 153
sum = 0
temp = num

while temp:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print('Armstrong')
else:
    print('not a armstrong')