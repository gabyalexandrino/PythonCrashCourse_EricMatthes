name = 'gabriella'
print("Your name == 'Gabriella'? I predict True.")
print(name.title() == 'Gabriella')
print("Your name == 'Maria'? I predict False.")
print(name.title() == 'Maria')

minuscula = 'NomePequeno'
print("\nIs minuscula == 'nomepequeno' using lower() method? I predict True.")
print(minuscula.lower() == 'nomepequeno')
print("Is minuscula == 'nomepequeno'? I predict False.")
print(minuscula == 'nomepequeno')

print('------------------------------------------------------------------------------------------------------------')

age = 34
print("\nYour age == 34? I predict True.")
print(age == 34)
print("Your age != 34? I predict False.")
print(age != 34)
print("Your age > 34? I predict False.")
print(age > 34)
print("Your age >= 34? I predict True.")
print(age >= 34)
print("Your age > 34? I predict False.")
print(age < 34)
print("Your age >= 34? I predict True.")
print(age <= 34)

print('------------------------------------------------------------------------------------------------------------')

name = 'gabriella'
print("Your name == 'Gabriella'? I predict True.")
print(name.title() == 'Gabriella')

age = 34
print("Your age == 34? I predict True.")
print(age == 34)

print("\nYour name == 'Gabriela' and your age == 34? I predict True.")
print(name.title() == 'Gabriella' and age == 34)
print("Your name == 'Gabriela' and your age == 35? I predict False.")
print(name.title() == 'Gabriella' and age == 35)
print("Your name == 'Maria' and your age == 34? I predict False.")
print(name.title() == 'Maria' and age == 34)

print('------------------------------------------------------------------------------------------------------------')

name = 'gabriella'
print("Your name == 'Gabriella'? I predict True.")
print(name.title() == 'Gabriella')

age = 34
print("Your age == 34? I predict True.")
print(age == 34)

print("\nYour name == 'Gabriela' or your age == 34? I predict True.")
print(name.title() == 'Gabriella' or age == 34)
print("Your name == 'Gabriela' or your age == 35? I predict True.")
print(name.title() == 'Gabriella' or age == 35)
print("Your name == 'Maria' or your age == 34? I predict True.")
print(name.title() == 'Maria' or age == 34)
print("Your name == 'Maria' or your age == 35? I predict False.")
print(name.title() == 'Maria' or age == 35)

print('------------------------------------------------------------------------------------------------------------')

onemillionlist = [number for number in  range(1,1000001)]
print("\nIs 500000 on the list? I predict True.")
print(500000 in onemillionlist)

print("\nIs 500000 not on the list? I predict False.")
print(500000 not in onemillionlist)

print("\nIs 1000001 on the list? I predict False.")
print(1000001 in onemillionlist)

print("\nIs 1000001 not on the list? I predict True.")
print(1000001 not in onemillionlist)
