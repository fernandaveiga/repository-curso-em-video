# escreva um programa que faça o computador 'pensar' em um numero inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero
# escolhido pelo  computador
# O programa deverá escrever na tela se o usuario venceu ou perdeu

n = (0,1,2,3,4,5)
from random import choice
sorteado = choice(n)

numero = int(input('Tente adivinhar qual nome entre 0 e 5 o computador pensou: '))

print('O numero escolhido pelo computador foi {} e voce digitou {}'.format(sorteado,numero))

if numero ==sorteado:
    print('Você acertou! Parabéns')
else:
    print('Você errou feio, errou rude!')
print('Obrigada por participar!')

# Ou também
#from random import randint
#computador = randint(0,5) - faz o computador 'pensar'
#print('Vou pensar em um numero entre 0 e 5, tente adivinhar')
#jogador = int(input('em que numero eu pensei?')
#if jogador ==computador:
#   print('parabens, voce acertou')
#else:
# print('eu pensei no numero {} e nao no {}.'.format(computador,jogador)

