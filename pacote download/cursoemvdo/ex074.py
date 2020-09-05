# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
# valor que estão na tupla.

from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(numeros)
print(f'O máximo valor foi {max(numeros)} e o mínimo valor foi {min(numeros)}')

'''
from random import randint
n1=randint(0,20)
n2=randint(0,20)
n3=randint(0,20)
n4=randint(0,20)
n5=randint(0,20)
n=(n1,n2,n3,n4,n5)
print(n)
maior=0
menor=21

for c in n:
    if c>maior:
        maior=c
    if c<menor:
        menor=c
print(f'O maior número da tupla é {maior} e o menor é {menor}') '''