teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste) # Coloca o teste dentro de outra lista, o galera
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste) # Os dois valores são substituídos, pois as duas estruturas são ligadas. Para que ficassem diferentes, seria necessário fazer uma cópia, usando galera.append(teste[:])
print(galera)
