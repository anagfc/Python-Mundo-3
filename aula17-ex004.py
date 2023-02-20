a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# Quando uma lista é igualada a outra, o Python estabelece uma ligação entre elas. Ligação é diferente de cópia.
c = a[:] # C recebe todos os valores de a. É uma cópia.
print(f'Lista C: {c}')
c[2] = 4
print(f'Lista A: {a}')
print(f'Lista C: {c}')
