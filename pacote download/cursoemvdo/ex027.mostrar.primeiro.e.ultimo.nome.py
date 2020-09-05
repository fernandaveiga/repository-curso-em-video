#Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o ultimo nome

nome = str(input('Digite seu nome completo: ')).strip()

separa = nome.split()

print('O nome completo digitado é {}'.format(nome))
print('o primeiro nome é {}'.format(separa[0]))
print('e o ultimo sobrenome é {}'.format(separa[len(separa)-1]))