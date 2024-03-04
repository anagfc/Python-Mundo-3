cadastros = list()
dados = list()
leves = list()
pesadas = list()
cadastrados = 0

# Captação de dados
while True:
    dados.append(str(input('\nInsira o nome: ')))
    dados.append(float(input(f'Insira o peso de {dados[0]} em Kg: ')))
    cadastros.append(dados[:])
    cadastrados += 1
    # Uma alternativa seria, ao fim, pedir len(cadastros)
    dados.clear()
    continuar = str(input('Continuar cadastros? [S/N] ')).upper()
    if continuar in 'Nnnão':
        break

# Análise
pesado = cadastros[0][1]
leve = cadastros [0][1]

for pessoas in cadastros:
# Achando o mais pesado
    if pesado < pessoas[1]:
        peso = pessoas[1]
        pesado = peso
        nome = pessoas[0]
        pesadas.clear()
        pesadas.append(nome[:])
    elif pesado == pessoas[1]:
        nome = pessoas[0]
        pesadas.append(nome[:])
# Achando o mais leve       
    elif leve > pessoas[1]:
        peso = pessoas[1]
        leve = peso
        nome = pessoas [0]
        leves.clear()
        leves.append(nome[:])
    elif leve == pessoas[1]:
        nome = pessoas[0]
        leves.append(nome[:])

# Resultado
print(f'\nForam cadastrados, no total, {cadastrados} pessoas.')
print(f'As pessoas mais pesadas são {pesadas}, com {pesado}Kg.')
print(f'As pessoas mais leves são {leves}, com {leve}Kg.')
