# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre:
# a) Qual é o total gasto na compra
# b) Quantos produtos custam mais de R$ 1000
# c)  Qual é o nome do produto mais barato
soma=0
p1000=0
r='S'
a=''
n=0
menor=10000000000
while r=='S':
    n= str(input('Nome do produto: '))
    p= float(input('Preço do produto: R$'))
    soma=soma+p
    if p>1000:
        p1000=p1000+1
    if p<menor:
        menor=p
        a=n
    r= str(input('Deseja continuar a colocar valores? [S/N]')).upper()
    if r!='S' and r!='N':
        r=str(input('Você deve digitar S ou N, digite novamente: ')).upper()
print(f'O gasto total da compra é R${soma}, há {p1000} produtos que custam mais de R$1000,00')
print(f'O produto mais barato é {a} que custa {menor}')