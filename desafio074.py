from random import randint
números = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Sua tupla: {números}')
maior = números[0]
menor = números[0]
for item in range(0, len(números)):
    if números[item] < menor:
        menor = números[item]
    if números[item] > maior:
        maior = números[item]
print(f'Maior número da sua tupla: {maior}')
print(f'Menor número da sua tupla: {menor}')
# É possível usar max(números) e min(números) para indicar, respectivamente, o maior e o menor números da tupla
