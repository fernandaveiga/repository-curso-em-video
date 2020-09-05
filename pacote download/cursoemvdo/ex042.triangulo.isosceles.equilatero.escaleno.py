# Refaça o o desafio 35 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo será formado:
# equilatero: todos os lados iguais
# isosceles: dois lados iguais
# escaleno: todos os lados diferentes

# 35(Desenvolv um programa que leia o comprimento de tres retas e diga ao usuário de elas podem ou
# nao formar um triangulo

r1=float(input('Digite o comprimento da primeira reta: '))
r2=float(input('Digite o comprimento da segunda reta: '))
r3=float(input('Digite o comprimento da terceira reta: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('As retas digitadas são {}, {} e {} e podem formar um triangulo.'.format(r1,r2,r3))
    if r1==r2==r3:
        print('Estas retas formarão um triangulo aquilátero.')
    elif r1 != r2!= r3 != r1:
        print('Estas retas formarão um triangulo escaleno.')
    else:
        print('Estas retas formarão um triangulo isósceles.')
else:
    print('As retas digitadas nao podem formar um triangulo')