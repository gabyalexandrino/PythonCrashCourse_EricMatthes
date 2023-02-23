favorite_places = {
    'joao': ['cumbuco', 'canoa quebrada', 'morro branco'],
    'jose': ['lagoinha', 'jericoacoara', 'pedra furada'],
    'maria': ['praia do preá', 'lagoa do paraíso', 'arvore da preguiça'],
    'francisca':['lagoa azul','tatajuba','trilha do mangue seco'],    
}
for name,places in favorite_places.items():
    print("\nOs lugares favoritos de " + name.title() + " são:")
    for place in places:
        print("\t" + place.title())

# for name, places in favorite_places.items():
#     print(f"\n{name.title()} likes the following places:")
#     for place in places:
#         print(f"- {place.title()}")