#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas
#Quantas letras há ao todo sem considerar espaços
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em letra maiúsculas: ', nome.upper())
print('Seu nome em letras minúsculas: ', nome.lower())
print('Seu nome tem um total de {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

