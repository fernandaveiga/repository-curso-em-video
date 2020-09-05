# Crie um programa que leia vários inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando a flag)
soma=0
n=0
c=0

while True:
    n = int(input('Digite um número inteiro: '))
    if n==999:
        break
    c=c+1
    soma=soma+n
print(f'Foram digitados {c} números e a soma entre eles é {soma}')