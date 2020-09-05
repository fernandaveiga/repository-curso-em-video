# Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceito numero: '))

print('Você digitou {}, {} e {}.'.format(n1,n2,n3))
if n1>n2 and n1>n3:
    print('o maior numero é {}'.format(n1))
if n2>n1 and n2>n3:
    print('O maior numero é {}'.format(n2))
if n3>n1 and n3>n2:
    print('O maior numero é {}'.format(n3))
if n1<n2 and n1<n3:
    print('O menor numero é {}'.format(n1))
if n2<n1 and n2<n3:
    print('O menor numero é {}'.format(n2))
if n3<n1 and n3<n2:
    print('O menor numero é {}'.format(n3))