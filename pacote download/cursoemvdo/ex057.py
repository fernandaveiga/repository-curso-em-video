# Faça um programa que leia o sexo de uma pessoa, mas só aceite de m ou f. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

s=0
while s!='M' and s!='F':
    s=str(input('Digite o seu gênero (M ou F): ')).upper()
print('O seu gênero é {}'.format(s))

'''sexo=str(input('Informe seu sexo[M ou F]: ')).strip().upper()
while sexo not in 'mMfM':
    sexo=str(input('Dados inválidos, digite novamente: '))
print('Sexo {} registrado com sucesso'.format(sexo))'''