def even_range(start,end):
    result = []
    for i in range(start,end+1):
        if i % 2 == 0:
            result.append(i)
    return result
print(even_range(4,10))