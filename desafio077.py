palavras = ('notebook', 'pasta', 'garrafa', 'caneta', 'flor', 'folha', 'vaso', 'planta', 'celular', 'carregador', 'arvore')
for item in palavras:
    print(f'\nAs vogais da palavra {item.upper()} são: ', end= '')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
        