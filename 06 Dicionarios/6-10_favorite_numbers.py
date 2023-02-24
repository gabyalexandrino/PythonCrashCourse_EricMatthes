favorite_numbers = {
    'gabriella':[11,23,45,53,57,59],
    'juvenilia':[9,13,25,39,46,54],
    'bruno':[7,8,14,19,32,45],
    'caio':[5,9,14,30,38,50],
    'maria':[6,12,32,44,51,57],
    'mandy': [19],
    'micah': [4,5,17,20,48,52],
    'gus': [2],
}
for nome, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print("\nO número favorito do(a) " + nome.title() + " é: " + str(number) + ".")
    else:
        print("\nOs números favoritos do(a) " + nome.title() + " são:")
        for number in numbers:
            print("\t" + str(number))