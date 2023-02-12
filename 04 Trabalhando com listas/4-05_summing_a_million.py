onemillionlist = []
for value in range(1,1000001):
    onemillionlist.append(value)

print(min(onemillionlist))
print(max(onemillionlist))
print(sum(onemillionlist))

#list_comprehension
onemillionlist_ = [value for value in range(1,1000001)]
print(min(onemillionlist_))
print(max(onemillionlist_))
print(sum(onemillionlist_))
