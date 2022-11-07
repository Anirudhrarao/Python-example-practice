num = int(input('enter your number'))
sum = 0
divisors = []
for i in range(1,num):
    if num%i == 0:
        sum += i
        divisors.append(i)
if num == sum:
    print(''.join(str(divisors)))
    print('perfect number')
else:
    print('not a perfect number')