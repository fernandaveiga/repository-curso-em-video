# crie um programa que leia um numero inteiro qualquer e mostre
# na tela se ele é par ou impar

numero= int(input('Digite um numero inteiro qualquer: '))

if numero%2==0:
    print('O numero digitado foi {} e ele é par.'.format(numero))
else:
    print('O numero digitado é {} e ele é ímpar'.format(numero))