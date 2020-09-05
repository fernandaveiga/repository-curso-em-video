# operações aritméticas
def soma(a, b):
    soma=a+b
    print(f'A soma entre {a} e {b} é {soma}')


soma(4, 5)
soma(9, 0)
print()
print('-' *40)
# a operação não precisa ter o nome da função como mostra o codigo com o mesmo resuldado do anterior:
def x(a, b):
    soma = a + b
    print(f'A soma entre {a} e {b} é {soma}')


x(3, 5)
x(2, 9)
print('-'*40)
# a ordem das variáveis podem mudar, desde que seja identificada quando for chamar a função
def divisao(a, b):
    divid = a / b
    print(f'{a}/{b} = {divid}')


divisao(5, 2)
divisao(b=5, a=2)
print('-'*40)
# quando não sabe quantos parametros vao ser colocados, neste caso o pycharm cria uma tupla com
# todos os números, sem limite de variáveis
def contador(*n):
    print(n)


contador(3, 5, 9)
contador(4, 8, 1, 12, 26)
print('-'*40)
# saber o tamanho da tupla criada
def contador(*n):
    tam = len(n)
    print(f'O tamanho da tupla é {tam}')


contador(3, 8, 1, 9, 12)
contador(2, 1, 6)
print('-'*40)
# pode também criar uma função que receba uma lista
# Então, para dobrar os valore da lista:
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos]*2
        pos = pos + 1


n = [6, 4, 3, 7]
dobra(n)
print(n)
print('-' * 40)
# para somar valores dados
def soma(*valores):
    s=0
    for valor in valores:
        s=s+valor
    print(f'Somando {valores} obtemos {s}')
print('-'*40)


soma(4, 7, 9, 2)
