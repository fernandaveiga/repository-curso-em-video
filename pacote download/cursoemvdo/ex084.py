# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) Uma listagem com as pesoas mais pesadas
# c) Uma listagem com as pessoas mais leves
lista = []
lista2 = []
r='S'
c=0
maior = menor = 0

while True:
    if r=='S':
        nome = lista.append(str(input('Nome: ')))
        c=c+1
        peso = lista.append(float(input('Peso: ')))
        r=str(input('Deseja digitar mais um número? [S/N] ')).upper()
        lista2.append(lista[:])
        lista.clear()
    elif r=='N':
        break
    else:
        r=str(input('Digite uma opção válida, S ou N: ')).upper()
for d in lista2:
    if len(lista2)==0:
        maior=menor=d[1]
    else:
        if d[1]>maior:
            maior=d[1]
        if d[1]<menor:
            menor=d[1]
print(lista2)
print(f'Ao todo você cadastrou {c} pessoas. ')
print(f'O maior peso foi {maior}kg, da pessoa ', end='')
for x in lista2:
    if x[1]==maior:
        print(f'{ [x[0]]}', end='')
print()
print(f'O menor peso foi {menor}kg, da pessoa', end='')
for x in lista2:
    if x[1]==menor:
        print(f' [{x[0]}]', end='')
print()

