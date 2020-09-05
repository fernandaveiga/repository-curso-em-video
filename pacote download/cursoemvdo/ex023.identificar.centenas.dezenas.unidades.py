# Fazer um programa que recebe um numero de 0 a 9999, identifica os milhares, centenas, dezenas e unidades.

numero = int(input('Digite um numero: '))

print('Analisando o numero digitado que é {}'.format(numero))

n1000= numero//1000
print('Vemos que o número do milhar é igual a {},'.format(n1000))

n100= (numero%1000)//100
print('o número da centena é {},'.format(n100))

n10= ((numero%1000)%100)//10
print('o número da dezena é {}'.format(n10))

n1= (((numero%1000)%100)%10)//1
print('e o número da unidade é {}'.format(n1))