rios = {'nilo':'egito', 'amazonas':'brasil','yangtze':'china', 'missisipi':'usa'}
for rio in sorted(rios):
    print("O rio " + rio.title() + " corre pelo " + rios[rio].title() + ".")

print("\nOs rios do dicionário são:")
for rio in sorted(rios):
    print(rio.title())

print("\nOs países do dicionário são:")
for rio in sorted(rios.values()):
    if rio == 'usa':
        print(rio.upper())
    else:
        print(rio.title())