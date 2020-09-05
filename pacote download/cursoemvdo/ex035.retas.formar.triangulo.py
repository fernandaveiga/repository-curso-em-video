#Desenvolva um programa que leia o comprimento de tres retas e diga
#ao usuário de elas podem ou nao formar um triangulo

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1<r2+r3 and r2<r3+r1 and r3<r1+r2:
    print('\033[1;36;47mAs tres retas digitadas foram {}, {} e {} e podem formar um triangulo.'.format(r1,r2,r3))
else:
    print('As retas digitadas não podem formar um triangulo')