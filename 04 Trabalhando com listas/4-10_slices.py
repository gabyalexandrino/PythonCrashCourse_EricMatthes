onemillionlist = [value for value in range(1,1000001)]

print("Os três primeiros itens da lista são:")
first3numbers = [number for number in onemillionlist[:3]]
print(first3numbers)

print("Três itens do meio da lista são:")
middlenumbers = [number for number in onemillionlist[499998:500001]]
print(middlenumbers)

print("Os três útimos itens da lista são:")
lastnumbers = [number for number in onemillionlist[999997:]]
print(lastnumbers)