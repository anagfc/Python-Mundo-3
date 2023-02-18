números = ('zero', 'um', 'dois', 'três', 'quatro','cinco', 'seis', 'sete', 'oito','nove', 'dez', 'onze', 'doze','treze', 'quatorze', 'quinze', 'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input('Insira um número de 0 até 20: '))
while escolha < 0 or escolha > 20:
    escolha = int(input('Inválido, tente novamente. Insira um número de 0 até 20: '))
print(f'O número escolhido foi {números[escolha]}.')
