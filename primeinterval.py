def prime(start,end):
    prime_num = []
    for num in range(start,end+1):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                prime_num.append(num)
    print(prime_num[:-1])

print(prime(2,7))