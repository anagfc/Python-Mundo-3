números = []
quantidade = 0
while True:
    inserir = int(input('Insira um número na sua lista: '))
    números.append(inserir)
    quantidade += 1
    novo = input('Continuar [S/N]: ').upper()
    if novo in 'NAONÃO':
        break
    elif novo in 'SIM':
        True
    else:
        print('Resposta não identificada.')
        novo = input('Continuar [S/N]: ').upper()
print('\nAnalisando...')
print(f'Foram acrescentados na sua lista {quantidade} números.')
if 5 in números:
    print('O número 5 faz parte da sua lista.')
else:
    print('O número 5 não está na sua lista.')
números.sort(reverse=True)
print(f'Sua lista em ordem descrescente é: {números}')
