brasileirão = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('{:^30}'.format('Brasileirão 2022'.upper()))
print('=' * 30)
print('{:^30}'.format('Cinco melhores colocados:'))
for colocação, time in enumerate(brasileirão):
    if colocação < 5:
        print('{}º Lugar: {}'.format(colocação+1, time))
print('-' * 30)
print('{:^30}'.format('Rebaixados'))
for colocação in range(20, 16, -1):
    print(f'{colocação}º Lugar: {brasileirão[colocação-1]}')
print('-' * 30)
print('{:^30}'.format('Participantes'))
print(sorted(brasileirão))
print('-' * 30)
print('{:^30}'.format('Localizando: '))
print('Palmeiras: {}º'.format(brasileirão.index('Palmeiras')+1))
print('Atlético-MG: {}º'.format(brasileirão.index('Atlético-MG')+1))
