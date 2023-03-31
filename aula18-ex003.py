galera = [['João', 19], ['Ana', 25], ['Joaquim', 13], ['Maria', 45]]
print(galera[0]) #Todas as informações
print(galera[0][0]) #Apenas o nome

for pessoa in galera:
    print(pessoa) #Exibe os itens da lista

for pessoa in galera:
    print(pessoa[0]) #Exibe somente os nomes

for pessoa in galera:
    print(pessoa[1]) #Exibe somente as idades    
    
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
    