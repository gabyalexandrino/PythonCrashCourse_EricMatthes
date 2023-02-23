
pets = []

pet01 = {'tipo':'passaro','nome':'liro','dono':'alexandrino'}
pets.append(pet01)
pet02 = {'tipo':'cachorro','nome':'sofia','dono':'gabriella'}
pets.append(pet02)
pet03 = {'tipo':'gato','nome':'miau','dono':'juvenilia'}
pets.append(pet03)
pet04 = {'tipo':'gato','nome':'mia','dono':'juvenilia'}
pets.append(pet04)
pet05 = {'tipo':'gato','nome':'neguinha','dono':'gabriella'}
pets.append(pet05)
pet06 = {'tipo':'passaro','nome':'sandy','dono':'neyla'}
pets.append(pet06)
pet07 = {'tipo':'passaro','nome':'junior','dono':'neyla'}
pets.append(pet07)
pet08 = {'tipo':'gato','nome':'apollo','dono':'laercio'}
pets.append(pet08)
pet09 = {'tipo':'gato','nome':'simba','dono':'laercio'}
pets.append(pet09)
pet10 = {'tipo':'cachorro','nome':'analu','dono':'regis'}
pets.append(pet10)
pet11 = {'tipo':'cachorro','nome':'zaraki','dono':'bruno'}
pets.append(pet11)

for pet in pets:
    tipo = pet['tipo']
    nome = pet['nome'].title()
    dono = pet['dono'].title()
    print(f"O(A) {nome} é um animal do tipo {tipo} que pertence ao dono {dono}.")

# for pet in pets:
#     print(f"\nHere's what I know about {pet['nome'].title()}:")
#     for key, value in pet.items():
#         print(f"\t{key}: {value}")
