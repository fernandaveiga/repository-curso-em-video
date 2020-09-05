# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda funçao vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior

lista = []
def sorteia():
    from random import randint
    print(f'Os valores sorteados foram: ', end = '')
    for c in range(1, 6):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end = ' ')
    print()
def somapar():
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma = soma + c
    print(f'A soma entre os números da lista é igual a {soma}')


sorteia()
somapar()

'''***COM PARAMETRO***
lista = []
def sorteia(lista):
    from random import randint
    print(f'Os valores sorteados são: ')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
    print()
    print('-'*32)
def somapar(lista):
    soma = 0
    print('A soma é igual a : ', end='')
    for c in lista:
        if c%2 == 0:
            soma = soma + c
    print(soma)
    print()


numeros = list()
sorteia(numeros)
somapar(numeros)'''