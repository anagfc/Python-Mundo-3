números = []
while True:
    inserir = int(input('Digite o número que deseja inserir: '))
    if inserir in números:
        print('Esse valor já está na lista.')
    else:
        números.append(inserir)
    novo = input('Novo número? [S/N] ').upper()
    if novo in 'NNAONÃO':
        break
números.sort()
print(f'Sua lista é: {números}')
