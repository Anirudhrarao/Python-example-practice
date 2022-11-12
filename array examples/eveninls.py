def even(ls):
    even_ls = []
    odd = []
    for num in ls:
        if num % 2 == 0:
            even_ls.append(num)
        else:
            odd.append(num)
    print('this is odd',odd)
    return even_ls
print('this is even ',even([12,67,78,34,90,34,56,107]))