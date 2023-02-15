users_names = ['admin', 'joao', 'jose', 'maria', 'mariana']

for user in users_names:
    print("Hello " + user.title() + "!")

print('------------------------------------------------------------------------------------------------------------')


for user in users_names:
    if user == 'admin':
        print("Hello " + user.title() + ", do you want a status report?")
    else:
        print("Hello " + user.title() + ", thank you for login again!")