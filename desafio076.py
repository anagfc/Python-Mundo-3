estoque = ('Caderno 10 matérias', 17, 'Kit 3 canetas Bic preta', 4.70, 'Kit canetas Bic coloridas', 18, 'Kit Lápis Faber-Castell', 3.60, 'Kit canetas Tilibra azul', 6.4, 'Pasta de arquivo Dac', 14.18, 'Kit canetas Compactor coloridas', 16.99, 'Régua 30cm Acrinil', 3.99)
print('{:^70}'.format('Consulta de itens').upper())
print('-' * 70)
for item in range (0, len(estoque)):
    if item % 2 == 0:
        print('{:.<65}R$ {:>4.2f}'.format(estoque[item], estoque[item+1]))
