guest_list = ['margarida', 'fatima', 'marilia', 'gilvan']

print("Por favor, venha jantar " + guest_list[0].title() + ".")
print("Por favor, venha jantar " + guest_list[1].title() + ".")
print("Por favor, venha jantar " + guest_list[2].title() + ".")
print("Por favor, venha jantar " + guest_list[3].title() + ".")

print("Encontrei uma mesa maior, vamos!")

guest_list.insert(0, "Clarissa")
guest_list.insert(3, "Carol")
guest_list.append("Daniel")

print(guest_list)

print("Por favor, venha jantar " + guest_list[0].title() + ".")
print("Por favor, venha jantar " + guest_list[1].title() + ".")
print("Por favor, venha jantar " + guest_list[2].title() + ".")
print("Por favor, venha jantar " + guest_list[3].title() + ".")
print("Por favor, venha jantar " + guest_list[4].title() + ".")
print("Por favor, venha jantar " + guest_list[5].title() + ".")
print("Por favor, venha jantar " + guest_list[6].title() + ".")

print("Sinto muito, só posso chamar duas pessoas.")

popped_guest_list = guest_list.pop()
print("Sinto muito, " + popped_guest_list.title() + " você não pode mais ir.")
print(guest_list)

popped_guest_list = guest_list.pop()
print("Sinto muito, " + popped_guest_list.title() + " você não pode mais ir.")
print(guest_list)

popped_guest_list = guest_list.pop()
print("Sinto muito, " + popped_guest_list.title() + " você não pode mais ir.")
print(guest_list)

popped_guest_list = guest_list.pop()
print("Sinto muito, " + popped_guest_list.title() + " você não pode mais ir.")
print(guest_list)

popped_guest_list = guest_list.pop()
print("Sinto muito, " + popped_guest_list.title() + " você não pode mais ir.")
print(guest_list)

print("Por favor, venha jantar " + guest_list[0].title() + ".")
print("Por favor, venha jantar " + guest_list[1].title() + ".")

del guest_list[1]
del guest_list[0]
print(guest_list)
