def combinations_three(ls):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j) and (j!=k) and (i!=k):
                    print(ls[i],ls[j],ls[k])

combinations_three(['PYTHON','BEST','RPOGRAMMING'])