users_names = []

if users_names:
    for user in users_names:
        if user == 'admin':
            print("Hello " + user.title() + ", do you want a status report?")
        else:
            print("Hello " + user.title() + ", thank you for login again!")
else:
    print("We need to find some users!")