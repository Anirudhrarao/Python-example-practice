ls = [23,56,12,45,12,6]
# def smallest_item(ls):
#     ls.sort()
#     print(ls[0])
# smallest_item(ls)

def smallest(ls):
    min = ls[0]
    for i in range(len(ls)):
        if ls[i] < min:
            min = ls[i]
    return min
print(smallest(ls))