galera = list()
dado = list()
maiores = menores = 0
for c in range(0, 3):
    dado.append(str(input('Nome: '))) #Coleta o nome
    dado.append(int(input('Idade: '))) #Coleta a idade
    galera.append(dado[:]) # Copia a lista criada dentro da lista galera
    dado.clear() # Limpa a lista dado pra não repetir

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        maiores += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        menores += 1
print(f'{maiores} pessoas são maiores de idade e {menores} pessoas são menores de idade.')
