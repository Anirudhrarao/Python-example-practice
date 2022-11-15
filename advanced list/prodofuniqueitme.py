def product(ls):
    res = 1
    unique = []
    for item in ls:
        if item not in unique:
            unique.append(item)
    for element in unique:
        res *= element
    return res
print(product([1,2,2,1,1,3]))