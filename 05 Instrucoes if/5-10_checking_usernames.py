current_users = ['admin', 'joao', 'jose', 'maria', 'mariana']
new_users = ['gabriella','raimundo','davi','joao', 'jose']

for name in new_users:
    if name.lower() in current_users:
        print("O nome " + name.title() + " já foi utilizado! Forneça um novo nome!")
    else:
        print("O nome " + name.title() + " está disponível!") 