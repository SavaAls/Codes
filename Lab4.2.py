x = [1,23,412,124,543,123,2,23,5,6,334,23,4,534,53,1,25,10]
x.extend([1,2,5,65,3,4,6,8,7])
print(list(filter(lambda x: x % 2, x)))
