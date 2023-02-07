#Nunca mais esquecer de colocar os () depois do método strip
name_person = '\tAda Lovelace \t\n'
print("."+name_person+".")
print("."+name_person.rstrip()+".")
print("."+name_person.lstrip()+".")
print("."+name_person.strip()+".")

#Lembrar que quando nao estiver obtendo resultado esperado, se o Python esta interpretando os números de forma correta
favourite_number = 7
print("Meu número favorito é "+ str(favourite_number) +"!")