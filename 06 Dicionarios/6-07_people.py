person_01 = {'first_name':'gabriella', 'last_name':'alexandrino', 'age':34, 'city':'fortaleza'}
person_02 = {'first_name':'jose', 'last_name':'lima', 'age':72, 'city':'juazeiro'}
person_03 = {'first_name':'juvenilia', 'last_name':'maria', 'age':64, 'city':'taua'}

people = [person_01, person_02, person_03]

for person in people:
    full_name = person['first_name'] + " " + person['last_name']
    print("O nome da pessoa é " + full_name.title() + ", idade " + str(person['age']) + ", da cidade de " + person['city'].title())

# for person in people:
#     name = f"{person['first_name'].title()} {person['last_name'].title()}"
#     age = person['age']
#     city = person['city'].title()   
#     print(f"{name}, of {city}, is {age} years old.")