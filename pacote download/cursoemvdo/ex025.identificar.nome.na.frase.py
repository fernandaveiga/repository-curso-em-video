#Um programa que leia o nome e diga se tem silva no nome
nome = str(input('Digite seu nome inteiro: ')).strip()

print('Seu nome completo possui o sobrenome silva? {}'.format('SILVA' in nome.upper()))