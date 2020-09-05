# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) Uma lista com todas as mulheres
# d) Uma lista com todas as pessoas com idade acima da média
dicio = {}
lista  = []
r = 'S'
c = 0
soma = 0
mulheres = []
maismedia = []
while True:
    if r == 'S':
        dicio['nome'] = str(input('Nome: '))
        c=c+1
        sexo = str(input('Sexo[F/M]: ')).upper()
        while sexo!='M' and sexo!='F':
            sexo = str(input('Digite novamente, F ou M: ')).upper()
        dicio['sexo'] = sexo
        if sexo == 'F':
            mulheres.append(dicio["nome"])
        idade = int(input('Idade: '))
        soma = soma + idade
        media = soma/c
        dicio['idade'] = idade
        if idade >= media:
            maismedia.append(dicio)
        lista.append(dicio.copy())
        r = str(input('Deseja adicionar mais um nome? ')).upper()
    elif r == 'N':
        break
    else:
        r = str(input('Digite uma opção válida, S ou N: ')).upper()
print(lista)
print(f'{c} pessoas foram cadastradas')
print(f'A média das idades é igual a {media}')
print(f'As mulheres são {mulheres}')
print(f'As pessoas com idade maior que a média são: ')
for p in lista:
    if p['idade']>= media:
        for k, v in p.items():
            print(f'{k} = {v};', end='')
            print()
print('ENCERRADO')
