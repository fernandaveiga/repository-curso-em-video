# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
n = int(input('Digite um valor para tabuada: '))
c=0
n=0
while True:
    for c in range(1,11):
        multi=c*n
        print(f'{n} x {c} = {multi}')
    n = int(input('Digite outro valor para tabuada: '))
    if n<0:
        break
print('Você digitou um número negativo, FIM.')

'''while True
    n=int(input('Digite um valor para a tabuada'))
    if n<0:
        break
    for c in range(1,11)
        print(f'{n} x {c} = {n*c}')
print('ENCERRADO!')'''