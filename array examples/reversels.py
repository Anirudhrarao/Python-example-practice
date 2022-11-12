def reverse_ls(ls):
    ls.reverse()
    return ls
print(reverse_ls([1,2,3]))

def reversing_ls(ls):
    reverse = []
    for i in ls[::-1]:
        reverse.append(i)
    return reverse
print(reversing_ls([12,24,36]))
