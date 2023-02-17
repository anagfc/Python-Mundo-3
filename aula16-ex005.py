a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Concatenação
d = b + a #Ordem altera quem vem primeiro
print(a)
print(len(a)) #Mostra quantos elementos existem na tupla
print(b)
print(c)
print(c.count(5)) #Mostra quantas vezes o 5 aparece na tupla
print(d)
print(d.index(8)) #Em que posição está o 8. Caso repita, pega sempre a 1ª ocorrência.
print(d.index(5, 1)) #Posição do 5 a partir do item 1
