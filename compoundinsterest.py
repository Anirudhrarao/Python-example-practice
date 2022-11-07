def compound_insterest(principle,rate,time):
    amount = principle * (pow((1+rate/100),time))
    ci = amount - principle
    return ci
print(compound_insterest(10000,10.25,5))