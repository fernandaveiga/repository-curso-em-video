# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
# progressão usando a estrutura

c=0
t=int(input('Qual o primeiro termo da PA? '))
r=int(input('Qual a razão da PA? '))
while c<10:
    pa=t+c*r
    c=c+1
    print(pa, end=' -> ')
print('ACABOU')