teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # Coloca o teste dentro de outra lista, o galera
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste) # Agora sim os valores mostrados serão diferentes, pois o valor inicial de teste foi copiado e não importado
print(galera)