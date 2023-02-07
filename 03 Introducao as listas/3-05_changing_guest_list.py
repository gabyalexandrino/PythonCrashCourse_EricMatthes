guest_list = ['margarida', 'fatima', 'marilia', 'gilvan']

print("Por favor, venha jantar " + guest_list[0].title() + ".")
print("Por favor, venha jantar " + guest_list[1].title() + ".")
print("Por favor, venha jantar " + guest_list[2].title() + ".")
print("Por favor, venha jantar " + guest_list[3].title() + ".")
print("Sinto muito, " + guest_list[2].title() + " não vem.")

not_comming = "marilia"
new_guest = "josé"
del guest_list[2]
print(guest_list)
guest_list.insert(2, new_guest)
print(guest_list)

print("Por favor, venha jantar " + guest_list[0].title() + ".")
print("Por favor, venha jantar " + guest_list[1].title() + ".")
print("Por favor, venha jantar " + guest_list[2].title() + ".")
print("Por favor, venha jantar " + guest_list[3].title() + ".")