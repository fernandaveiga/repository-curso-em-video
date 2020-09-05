# Faça um programa que leia o ano de nascimento de um jovem e informe
# de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar se é a hora de se alistar
# Se ja passou do tempo de alistamento
# seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Qual o ano que voce nasceu? '))
idade=2020-ano

if idade==18:
    print('Você tem 18 anos e deve se alistar ao exercito agora.')
elif idade>18:
    mais=idade-18
    print('Você tem mais de 18 anos e passou {} anos da hora de se alistar.'.format(mais))
else:
    menos=18-idade
    print('Você tem {} anos e ainda falta {} anos para ter 18 e ter que alistar.'.format(idade,menos))