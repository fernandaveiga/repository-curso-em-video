# Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
# o primeiro valor é maior
# O segundo valor é maior
# não existe valor maior, os dois são iguais

n1=int(input('Digite um numero inteiro: '))
n2=int(input('Digite outro numero inteiro: '))

if n1>n2:
    print('O primeiro valor digitado foi {} e é maior que o segundo digitado que foi {}.'.format(n1,n2))
elif n2>n1:
    print('O segundo valor digitado foi {} e é maior que o primeiro digitado que foi {}.'.format(n2,n1))
else:
    print('Os valores digitados são iguais e equivalem a {}'.format(n1))