def pattern(num):
    for i in num:
        print("|",end=' ')
        print("*"*int(i))

pattern("12345")