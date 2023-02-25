números = [int(input('Insira um valor: ')), int(input('Insira mais um valor: ')), int(input('Insira o próximo valor: ')), int(input('Insira outro valor: ')), int(input('Insira o último valor: '))]
print(f'A lista inserida foi {números}')
print(f'Maior número da lista: {max(números)}, na(s) posição(ões): ', end ='')
for pos, item in enumerate(números):
    if item == max(números):
        print(pos, end='. ')
print(f'\nMenor número da lista: {min(números)}, na(s) posição(ões): ', end='')
for pos, item in enumerate(números):
    if item == min(números):
        print(pos, end='. ')
