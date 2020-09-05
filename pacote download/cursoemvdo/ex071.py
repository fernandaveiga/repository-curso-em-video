# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# obs: Considere que o caixa possui cédula de 50, 20, 10 e 1

'''v= int(input('Qual o valor deve ser sacado? '))
x=v//50
y=v%50
z=y//20
a=y%20
b=a//10
c=a%10
print(f'{x} cédulas de 50 e resta {y}')
print(f'{z} cédulas de 20 e resta {a}')
print(f'{b} cédulas de 10 e resta {c} de 1')
print(f'{x} cédulas de 50, R${z} cédulas de 20, R${b} cédulas de R$10 e {c} de R$1')
'''
n= int(input('Qual o valor você deseja sacar?'))

if n%50>0:
    n5=n//50
    n=n%50
if n%20>0:
    n2=n//20
    n=n%20
if n%10>0:
    n1=n//10
    n=n%10
    print(f'São {n5} cédulas de 50, {n2} de 20, {n1} de 10 e {n} de 1')
