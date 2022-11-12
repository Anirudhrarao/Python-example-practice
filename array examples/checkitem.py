def search(item,ls):
    for i in ls:
        if i in ls:
            return f'{item} present in ls'
        else:
            print('There is no such item present in ls')
print(search(22,[45,67,89,22]))