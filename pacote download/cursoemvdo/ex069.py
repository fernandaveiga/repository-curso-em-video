# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
#a) Quantas pessoas tem mais de 80 anos
#b) Quantos homens foram cadastrados
#c) Quantas mulheres tem menos de 20 anos

m20=0
id=0
masc=0
r='S'
while r=='S':
    i= int(input('Idade: '))
    if i>80:
        id=id+1
    s= str(input('Sexo: [F/M]')).upper()
    if s!='F' and s!='M':
        s=str(input('Digite uma opção válida, F ou M: ')).upper()
    if s=='M':
        masc=masc+1
    if i<20 and s=='F':
        m20=m20+1
    r= str(input('Deseja continuar? [S/N] ')).upper()
    if r!='S' and r!='N':
        r=str(input('Digite uma opção válida, S ou N: '))
print(f'Há {id} pessoas com mais de 80 anos, {masc} homens e {m20} mulheres com menos de 20 anos')