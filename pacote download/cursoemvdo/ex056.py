#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

count1=0
count2=0
maior=0
soma=0
for n in range(1,5):
    nome=str(input('Digite o nome da {}ª pessoa: '.format(n)))
    idade=float(input('Digite a idade da {}ª pessoa: '.format(n)))
    sexo=str(input('Digite o sexo da {}ª pessoa(M ou F): '.format(n))).upper()
    soma= soma+idade
    media=soma/n
    if sexo=='M':
        count1=count1+1
        if idade>maior:
            maior= idade
            nom=nome
    if sexo=='F':
        if idade<20:
            count2=count2+1
print('São {} homens e o mais velho tem {} anos e se chama {}'.format(count1,maior,nom))
print('A média das idades entre os quatro é {}'.format(media))
print('Há {} mulheres com menos de 21 anos'.format(count2))