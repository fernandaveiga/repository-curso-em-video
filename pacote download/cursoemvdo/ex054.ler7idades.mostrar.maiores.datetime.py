# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

count1=0
count2=0
from datetime import date
atual=date.today().year
for c in range(1,8):
    n=int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - n
    if idade<18:
        count1=count1+1
    else:
        count2=count2+1
print('O numero de pessoas menores de idade é igual a {} e maiores de idade igual a {}'.format(count1,count2))