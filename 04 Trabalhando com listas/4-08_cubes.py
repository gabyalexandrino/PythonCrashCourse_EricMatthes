cubes = []
for value in range(1,11):
    cubes.append(value**2)
print(cubes)

#list_comprehension
cubes_ = [value**2 for value in range(1,11)]
print(cubes_)