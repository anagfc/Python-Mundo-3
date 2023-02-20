valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')
    
for c, v in enumerate(valores):
    print(f'Na posição {c} está o valor {v}.')
print('Cheguei ao final da lista')
