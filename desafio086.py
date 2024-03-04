matriz = []
coluna = []

for col in range (1, 4):
    for lin in range (1, 4):
        num = int(input(f'Insira o {lin}º número da {col}ª coluna: '))
        coluna.append(num)
    matriz.append(coluna[:])
    coluna.clear()

print('\n')
print('Sua matriz'.upper())
for c in range (0, 3):
    for item in range (0, 3):
        print(f'[{matriz[c][item]:^7}]', end = '     ')
    print('\n')
