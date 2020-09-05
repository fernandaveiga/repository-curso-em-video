# Crie um programa que leia duas notas e calcule sua média, mostrando
# uma mensagem no final, de acordo com a média atingida:
# media abaixo de 5: REPROVADO
# media entre 5 e 6.9: RECUPERAÇÃO
# media 7 ou superior: APROVADO

n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=(n1+n2)/2

if media<5:
    print('Sua média é {} e voce está REPROVADO.'.format(media))
elif 5<=media<=6.9:
    print('Sua média é {} e voce está de RECUPERAÇÃO'.format(media))
else:
    print('Sua média é {} e voce está APROVADO'.format(media))
