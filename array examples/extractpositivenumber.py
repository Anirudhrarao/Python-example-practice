def extract_postive_number(ls):
    result = []
    for num in ls:
        if num >= 0:
            result.append(num)
    return result
print(extract_postive_number([12,-67,-23,-435,465,-34,546]))