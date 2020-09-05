# A confederação nacional de natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo
# com sua idade:
# até 9 anos mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 20 anos: senior
# acima: master

ano=int(input('Digite o ano de nascimento do atleta: '))
idade=2020-ano

if 1900<ano<2021:
    if idade<=9:
        print ('CATEGORIA: MIRIM')
    elif 9<idade<=14:
        print('CATEGORIA INFANTIL')
    elif 14<idade<=20:
        print('CATEGORIA SENIOR')
    else:
        print('CATEGORIA MASTER ')
else:
    print('Você nao digitou um ano válido')

#from datetime import date
#atual = date.today().year
#nascimento = int(input(' ano de nascimento: ')
#idade = atual - nascimento
#print('o atleta tem {} anos'.format(idade))
#if idade <=9:
#   print('MIRIM')
#elif idade <=14:
#   print('INFANTIL')
#elif idade <=19:
#   print('JUNIOR')
#elif idade <=25:
#   print('SENIOR')
#else:
#print('MASTER')