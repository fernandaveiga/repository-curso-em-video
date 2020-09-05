# Desenvolva um programa que leia a distancia de uma viagem em km
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens
# até 200km e R$0,45 para viagens mais longas

distancia= float(input('Digite a distancia que será percorrida na viagem: '))

if distancia<=200:
    preco=distancia*0.50
    print('A distancia da viagem é {} e o valor que será cobrado é {}.'.format(distancia,preco))
else:
    preco=distancia*0.45
    print('A distancia da viagem é {} e o valor cobrado será {}.'.format(distancia,preco))