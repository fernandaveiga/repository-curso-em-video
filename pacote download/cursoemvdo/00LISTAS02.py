lista0 = []
lista1 = []
totmen = totmai = 0
for c in range(0,3):
    lista0.append(str(input('Nome: ')))
    lista0.append(int(input('Idade: ')))
    lista1.append(lista0[:])
    lista0.clear()
print(lista0)
print(lista1)

for d in lista1:
    if d[1] >= 18:
        print(f'{d[0]} é maior de idade.')
        totmai = totmai+1
    else:
        print(f'{d[0]} é menor de idade')
        totmen = totmen + 1
print(f'{totmai} são maiores de idade e {totmen} são menores de idade')