# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Digite o ano que gostaria de saber se é bissexto: '))

if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ano digitado é {} e ele é bissexto'.format(ano))
else:
    print('O ano digitado é {} e não é bissexto.'.format(ano))