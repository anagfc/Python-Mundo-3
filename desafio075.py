números = (int(input('Insira o 1º valor: ')), int(input('Insira o 2º valor: ')), int(input('Insira o 3º valor: ')), int(input('Insira o 4º valor: ')))
print(f'Sua tupla foi: {números}')
print(f'Na sua tupla existem {números.count(9)} números 9.')
if 3 in números:
    print(f'O 1º número 3 da sua tupla está na posição {números.index(3)+1}.')
else:
    print('Não existe nenhum nº3 na sua tupla.')
print('São pares na sua tupla os números ', end='')
for item in range(0, len(números)):
    if números[item] % 2 == 0:
        print(f'{números[item]}', end=' ')
