# Desenvolva um programa que leia o primeiro termo e a razão de uma pa. No final, mostre os 10 primeiros
# termos dessa progressão.

t1=int(input('Qual o primeiro termo da PA? '))
r=int(input('Qual a razão da PA? '))

for c in range(t1,(t1+r*10),r):
    print(c, end=' -> ')
print('ACABOU')