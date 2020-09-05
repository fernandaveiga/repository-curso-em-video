# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# impares digitados, respectivamente
# Ao final, mostre o conteúdo das tres listas geradas

r='S'
lista1=list()
lista2=list()
lista3=list()
while r=='S':
    n=int(input('Digite um número: '))
    lista1.append(n)
    if n%2==0:
        lista2.append(n)
    else:
        lista3.append(n)
    r=str(input('Deseja digitar mais números? S ou N: ')).upper()
    while r!='N' and r!='S':
        r=str(input('Digite novamente, S ou N: ')).upper()
print(f'A lista completa é {lista1}. ')
print(f'A lista de números pares é {lista2}. ')
print(f'A lista de números ímpares é {lista3}. ')