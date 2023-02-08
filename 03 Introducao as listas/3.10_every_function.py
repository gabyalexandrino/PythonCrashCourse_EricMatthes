nacionalidade = ['portuguesa', 'filipina', 'sul-africano', ' zimbabweano', 'namibiana', 'boliviano', 'brasileiro', 'chileno', 'colombiano', 'costarriquenho', 'cubano', 'dominicano' , 'equatoriano', 'salvadorenho', 'granadino', 'guatemalteco', 'guianês', 'guianense', 'haitiano', 'hondurenho', 'jamaicano', 'mexicano', 'nicaraguense', 'panamenho', 'paraguaio', 'peruano', 'portorriquenho', 'dominicana', 'são-cristovense', 'são-vicentino', 'santa-lucense', 'surinamês', 'trindadense', 'uruguaio', 'venezuelano', 'alemã', 'austríac', 'belga', 'croata', 'dinamarquês', 'antiguano', ' argentino', 'bahamense', 'barbadense', 'belizenho', 'eslovaco', 'esloveno', 'espanhol', 'francês', 'grego', 'húngaro', 'irlandês', 'italiano', 'noruego', 'holandês', 'polonês', 'inglês', 'galês', 'escocês', 'romeno', 'russo', 'sérvio', 'sueco', 'suíço', 'turco', 'ucraniano', 'americano', 'canadense', 'angolano', 'moçambicano', 'sul-africano', ' zimbabuense', 'argélia', 'comorense', 'egípcio', 'líbio', 'marroquino', 'ganés', 'queniano', 'ruandês', 'ugandense', 'bechuano', 'marfinense', 'camaronense', 'nigeriano', 'somali', 'australiano', 'neozelandês', 'afegão', 'saudita', 'armeno', 'bangladesh', 'chinês', 'norte-coreano', 'sul-coreano', 'indiano', 'indonésio', 'iraquiano', 'iraniano', 'israelita', 'japonês', 'malaio', 'nepalês', 'omanense', 'paquistanês', 'palestino', 'qatarense', 'sírio', 'cingalês', 'tailandês', 'timorense', 'arabe', 'vietnamita','iemenita']

print(nacionalidade)

print("\nExibindo primeiro elemento: " + nacionalidade[0])

print("\nExibindo último elemento: " + nacionalidade[-1])

print("\nFormatando um elemento da lista com o método title(): " + nacionalidade[0].title())


print("\nExibindo último elemento: " + nacionalidade[-1].title())
print("Adicionando um elemento 'bulgaro' na lista com o método append()...")
nacionalidade.append('bulgaro')
print("Exibindo último elemento: " + nacionalidade[-1].title())

print("\nExibindo primeiro elemento: " + nacionalidade[0].title())
print("Adicionando o elemento 'cambojano' na lista com o método insert() na primeira posição...")
nacionalidade.insert(0,'cambojano')
print("Exibindo primeiro elemento: " + nacionalidade[0].title())

print("\nExibindo último elemento: " + nacionalidade[-1].title())
print("Removendo o último elemento com o método del(): ")
del(nacionalidade[-1])
print("Exibindo último elemento: " + nacionalidade[-1].title())

print("\nExibindo último elemento: " + nacionalidade[-1].title())
print("Removendo o último elemento com o método pop(): ")
nacionalidade_popped = nacionalidade.pop()
print("Exibindo último elemento: " + nacionalidade[-1].title())
print("Exibindo o elemento excluído armazenado numa variável: " + nacionalidade_popped.title())

print("\nExibindo primeiro elemento: " + nacionalidade[0].title())
print("Removendo o primeiro elemento com o método pop(): ")
nacionalidade_popped = nacionalidade.pop(0)
print("Exibindo primeiro elemento: " + nacionalidade[0].title())
print("Exibindo o elemento excluído armazenado numa variável: " + nacionalidade_popped.title())





