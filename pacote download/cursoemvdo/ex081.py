# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# a)Quantos números foram digitados
# b)A lista de valores ordenada de forma decrescente
# c)Se o valor 5 foi digitado e está ou não na lista

r='S'
c=0
lista=list()
while r=='S':
    n=lista.append(int(input('Digite um número: ')))
    c=c+1
    r=str(input('Deseja continuar a adicionar números? [S/N]')).upper()
    while r!='S' and r!='N':
        r=str(input('Digite novamente, S ou N: ')).upper()
print(f'{c} números foram digitados.')
lista.sort(reverse=True)
print(f'A lista ordenada de forma descrescente é {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na lista. ')
else:
    print('O valor 5 não foi adicionado e não está na lista. ')

'''
valores = []
while True:
    valores.append(int(input('digite um valor:')))
    resp = str(input('Quer continuar? S ou N: '))
    if resp in 'Nn':
        break
print(f'você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista') '''