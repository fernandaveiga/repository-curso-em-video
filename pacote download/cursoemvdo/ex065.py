# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a media entre
# todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores
op='S'
soma=0
c=0
maior=0
menor=0
while op=='S':
    c=c+1
    n=int(input('Digite um número inteiro:'))
    if c==1:
        maior=n
        menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    soma=soma+n
    media=soma/c
    op=str(input('Você deseja digitar outro numero? [S/N]')).upper()
    if op=='N':
        print('A média entre os valores foi igual a {} e o maior numero é {} e o menor é {}'.format(media,maior,menor))
    elif op!='N' and op!='S':
        op=str(input('Digite uma opção válida, S ou N')).upper()

''' se nao colocar a opção op!=n e op!=s
op='S'
soma=0
c=0
maior=0
menor=0

while op=='S':
    n=int(input('Digite um numero inteiro: '))
    c=c+1
    soma=soma+n
    if c==1:
        maior=n
        menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    op=str(input('Você deseja adicionar mais um número? [S/N]')).upper()
media=soma/c
print('A média é igual a {}, o maior número é o {} e o menor é {}'.format(media, maior, menor))'''
