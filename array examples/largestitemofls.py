ls = [12,45,12,45,678665]
def largest(ls):
    max = ls[0]
    for i in range(len(ls)):
        if ls[i] > max:
            max = ls[i]
    return max
print(largest(ls))