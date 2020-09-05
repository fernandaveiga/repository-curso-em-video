# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e impares. No final, mostre os valores pares e ímpares em
# ordem crescente.
lista = [[],[]]

for c in range(0,7):
    n=(int(input(f'Digite o {c+1}º valor: ')))
    if n%2==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(lista)
print(f'Os valores pares da lista são {lista[0]}')
print(f'Os valores ímpares da lista são {lista[1]}')