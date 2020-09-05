# Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados
# A soma dos valores da terceira coluna
# O maior valor da segunda linha
maior=0
soma=0
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
for c in lista:
    for d in c:
        if d%2==0:
            soma=soma+d
print(f'A soma dos números pares é igual a {soma}.')
soma=lista[0][2]+lista[1][2]+lista[2][2]
print(f'A soma dos números da terceira coluna é igual a {soma}.')
for c in lista[1]:
    if c>maior:
        maior=c
print(f'O maior valor na segunda linha é igual a {maior}')
