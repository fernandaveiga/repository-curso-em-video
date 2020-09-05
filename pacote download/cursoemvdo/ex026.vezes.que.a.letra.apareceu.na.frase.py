#Faça um programa que leia uma frase e mostre
#Quantas vezes aparece a letra A
#Em qual posição ela aparece na primeira vez
#Em que posição ela aparece pela ultima vez

frase = str(input('Digite uma frase: ')).strip().lower()

print('A frase digitada tem {} vezes a letra a'.format(frase.count('a')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra A aparece pela ultima vez na posição {}'.format(frase.rfind('a')+1))