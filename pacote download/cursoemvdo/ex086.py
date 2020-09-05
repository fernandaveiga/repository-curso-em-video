# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tela, com a formatação correta
lista = [[], [], []]
for c in range(0,3):
    n = int(input(f'Digite o valor para [0, {c}] da matriz: '))
    lista[0].append(n)
for c in range(0,3):
    n = int(input(f'Digite o valor para [1, {c}] da matriz: '))
    lista[1].append(n)
for c in range(0,3):
    n = int(input(f'Digite o valor para [2, {c}] da matriz: '))
    lista[2].append(n)
print(f'[ {lista[0][0]:^4} ] [ {lista[0][1]:^4} ] [ {lista[0][2]:^4} ]')
print(f'[ {lista[1][0]:^4} ] [ {lista[1][1]:^4} ] [ {lista[1][2]:^4} ]')
print(f'[ {lista[2][0]:^4} ] [ {lista[2][1]:^4} ] [ {lista[2][2]:^4} ]')

'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=')
    print()'''