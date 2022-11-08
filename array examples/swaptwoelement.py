def swap_two(ls,pos1,pos2):
    ls[pos1],ls[pos2] = ls[pos2],ls[pos1]
    return ls
print(swap_two([12,24,36,48],1-1,2-1))