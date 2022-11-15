test_ls = [1,2,2,3,4,6,6,4,7,8,7]
new_ls = []
count = 0
for item in test_ls:
    if item not in new_ls:
        count += 1
        new_ls.append(item)

print(count)