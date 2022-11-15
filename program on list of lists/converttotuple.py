test_ls  = [["a","b",1,2],["c","d",3,4]]
res = dict()
for item in test_ls:
    res[tuple(item[:2])] = tuple(item[2:])
print(res)