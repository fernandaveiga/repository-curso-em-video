# Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e
# que se encontram no intervalo entre 1 até 500.
#Quantos numeros foram somados?

s=0
cont=0
for c in range(1,501,2):
    if c%3==0:
        s=s+c
        cont=cont+1
print('A soma de todos os {} valores é igual a {}'.format(cont,s))

