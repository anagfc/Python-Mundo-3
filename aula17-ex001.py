num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2,0)
print(num)
num.pop()
print(num)
print(f'Essa lista possui {len(num)} elementos.')
if 4 in num:
    num.remove(4)
else:
    print('Não achei nenhum 4 na lista.')
    