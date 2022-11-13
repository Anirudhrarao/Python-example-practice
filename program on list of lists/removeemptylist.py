def filter_list(ls):
    res = [item for item in ls if item != []]
    return res
print(filter_list([12,45,23,78,[],[],90,[90]]))

def extract_list(ls):
    res = []
    for item in ls:
        if item:
            res.append(item)
    return res
print(extract_list([12,[],34,[]]))