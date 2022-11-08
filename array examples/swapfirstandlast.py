def swaplist(ls):
    size = len(ls)
    temp = ls[0]
    ls[0] = ls[size - 1]
    ls[size - 1] = temp
    return ls
print(swaplist([12,34,5]))