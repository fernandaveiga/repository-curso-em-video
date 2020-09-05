# Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista:
# No final, mostre qual foi o maior e o menor valor
# digitado e as suas respectivas posições na lista

lista=[]
for c in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {c}: ')))
print(lista)
for pos, numero in enumerate(lista):
    if numero==max(lista):
        print(f'O maior valor foi {max(lista)} e está na posição {pos}')
    if numero==min(lista):
        print(f'O valor mínimo é {min(lista)} e está na posição {pos}')