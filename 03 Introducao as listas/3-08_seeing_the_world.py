places = ['japao', 'canada', 'eua', 'italia', 'china', 'alemanha', 'frança']

print(places)

print("\nExibindo a lista com o método sorted():")
print(sorted(places))

print("\nMostrando a lista original:")
print(places)

print("\nExibindo a lista com o método sorted() reverso:")
print(sorted(places,reverse=True))

print("\nMostrando a lista original:")
print(places)

print("\nExibindo a lista com o método reverse():")
places.reverse()
print(places)

print("\nExibindo a lista com o método reverse() pela segunda vez:")
places.reverse()
print(places)

print("\nExibindo a lista com o método sort():")
places.sort()
print(places)

print("\nExibindo a lista com o método sort():")
places.sort(reverse=True)
print(places)
