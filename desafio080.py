números = []
for cadastro in range(0,5):
    inserir = int(input('Número a inserir na lista: '))
    if cadastro == 0 or inserir >= números[-1]:
        print(f'{inserir} adicionado na posição {len(números)}.')
        números.append(inserir)
    else:
        posição = 0
        while posição < len(números):
            if inserir <= números[posição]:
                print(f'{inserir} adicionado na posição {posição}.')
                números.insert(posição, inserir)
                break
            posição += 1
print('-=' * 20)
print(números)
