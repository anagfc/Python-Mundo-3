print(f'{"Analisador de expressões":^50}'.upper())
expressão = input('Insira a expressão: ')
abertos = expressão.count('(')
fechados = expressão.count(')')
if abertos == fechados:
    print('Expressão válida!')
else:
    print('Expressão inválida.')
    