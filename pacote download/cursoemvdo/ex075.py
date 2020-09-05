#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
#a) quantas vezes apareceu o valor 9
#b) em que posição foi digitado o primeiro valor 3
#c) quais foram os números pares

n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
d=0
print(f'Você digitou os números {n}.')
if 9 in n:
    print(f'O número 9 apareceu {n.count(9)} vez(es).')
else:
    print('O número 9 não apareceu nesta tupla.')
if 3 in n:
    print(f'O número 3 aparece na {n.index(3)+1}ª posição desta tupla.')
else:
    print(f'O número 3 não aparece nessa tupla')
print('Os números pares são: ', end='')
for c in n:
    if c%2==0:
        d=d+1
        print(f'{c} ')
print(f'São {d} números pares')