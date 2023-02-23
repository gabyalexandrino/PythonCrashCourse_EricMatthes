favorite_languages = {'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'erick': 'swift',
    'mateus': 'java',
    'sarah': 'cobol',
    'joao': 'javascript',
    'maria': 'php',
    'jose': 'c++',
    }

for name, language in favorite_languages.items(): 
    print(name.title() + "'s favorite language is " + language.title() + ".")

coders = ['jen', 'sarah', 'josh', 'david', 'becca', 'edward', 'phil', 'erick', 'mateus', 'sarah', 'joao', 'maria', 'jose', 'matt', 'danielle']

print("\n")
for name in coders:
    if name in favorite_languages:
        print("Obrigada, " + name.title() + " por responder a enquete!")
    else:
        print("Por gentileza " + name.title() + ", responder a enquete!")