def sum_avg_ls(ls):
    sum = 0
    length = len(ls)
    for i in ls:
        sum += i
    avg = (sum)/length
    return avg
print(sum_avg_ls([4,5,1,2,9,7,10,8]))
