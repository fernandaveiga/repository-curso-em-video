# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# sequencia de fibonacci.

n=int(input('Digite um número:'))
f1=0
f2=1
print('{} -> {}'.format(f1,f2), end='')
c=3
while c<=n:
    f3=f2+f1
    print(' -> {}'.format(f3), end='')
    f1=f2
    f2=f3
    c=c+1
print(' FIM')