#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] pedra
[1] papel
[3] tesousa ''')
jogador = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador ==0:
    if jogador==0:
        print('EMPATE')
    elif jogador==1:
        print('Jogador vence')
    elif jogador==2:
        print('Computador vence')
    else:
        print('Jogada inválida')
elif computador ==1:
    if jogador==1:
        print('EMPATE')
    elif jogador==0:
        print('computador vence')
    elif jogador==2:
        print('Jogador vence')
    else:
        print('Jogada inválida')
elif computador ==2:
    if jogador==2:
        print('EMPATE')
    elif jogador==0:
        print('Jogador vence')
    elif jogador==1:
        print('computador vence')
    else:
        print('jogada inválida')
else:
    print('Jogada inválida')