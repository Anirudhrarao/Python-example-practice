def largest_elemets(ls):
    maxs = ls[0]
    for i in range(0,len(ls)):
        if ls[i] > maxs:
            maxs = ls[i]
    print(maxs)
largest_elemets([23,23,45,12,1009090])