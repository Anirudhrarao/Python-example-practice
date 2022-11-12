def count_odd_even(ls):
    even, odd = 0, 0
    for i in ls:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print('Even number in list: ',even)
    print('Odd number in list: ', odd)
count_odd_even([12,45,23,67,78,24])