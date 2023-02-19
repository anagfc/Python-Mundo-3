palavras = ('notebook', 'pasta', 'garrafa', 'caneta', 'flor', 'folha', 'vaso', 'planta', 'celular', 'carregador', 'arvore')
for item in range(0, len(palavras)):
    print(f'\n{palavras[item]}: '.title(), end= '')
    if palavras[item].count('a') != 0:
        print('a', end=' ')
    if palavras[item].count('e') != 0:
        print('e', end=' ')
    if palavras[item].count('i') !=0:
        print('i', end=' ')
    if palavras[item].count('o') !=0:
        print('o', end=' ')
    if palavras[item].count('u') !=0:
        print('u', end=' ')
        