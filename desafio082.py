números = []
par = []
ímpar = []
while True:
    inserir = int(input('Insira um número à sua lista: '))
    números.append(inserir)
    if inserir % 2 == 0:
        par.append(inserir)
    else:
        ímpar.append(inserir)
    novo = input('Continuar [S/N]: ').upper()
    if novo in 'SIM':
        True
    elif novo in 'NAONÃO':
        break
    else:
        print('Resposta inválida. Tente novamente.')
        novo = input('Continuar [S/N]: ').upper()
print('\nAnalisando...')
print(f'Sua lista: {números}')
print(f'Números pares inseridos: {par}')
print(f'Números ímpares inseridos:{ímpar}')
    