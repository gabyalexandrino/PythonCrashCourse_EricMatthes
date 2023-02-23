words = {'and':'returns true if both statements are true',
         'or':'returns true if one of the statements is true',
         'not':'reverse the result, returns false if the result is true',
         'is':'returns true if both variables are the same object',
         'is not':'teturns true if both variables are not the same object	',
         'in':'returns true if a sequence with the specified value is present in the object',
         'not in':'returns true if a sequence with the specified value is not present in the object',
         'for':'execução de um mesmo comando até que uma determinada condição seja atendida', 
         'if':'verificar uma expressão e executar um bloco de código caso a condição definida seja verdadeira', 
         'elif':'executar um bloco de código, caso o resultado da expressão informada na instrução if seja falso',
         'else':'realizar a verificação de outra expressão caso a primeira validação seja falsa',
         }



for name, language in words.items(): 
    print(name.title() + " significa em Python: " + language.title() + ".")

print("\n")
for word in words:
    print("O significado da palavra '" + word.title() + "' em Python é: " + words[word].capitalize() + ".")