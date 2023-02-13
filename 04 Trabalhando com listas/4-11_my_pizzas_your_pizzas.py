pizzas = ['Calabresa', 'Portuguesa', 'Marguerita', 'Frango com catupiry', 'Muçarela', 'Napolitana', 'Quatro queijos', 'Atum com cebola', 'Baiana', 'Caipira', 'Brigadeiro', 'Romeu e Julieta', 'Califórnia']
friend_pizzas = pizzas[:]
pizzas.append('Chocolate')
friend_pizzas.append('Supreme')
print("Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza)
print("\nAs pizzas favoritas de meu amigo são:")
for pizza in friend_pizzas:
    print(pizza)
