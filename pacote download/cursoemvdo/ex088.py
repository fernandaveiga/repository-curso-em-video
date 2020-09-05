# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
# lista composta.
lista = []
n=int(input('Digite quantos palpites você deseja fazer: '))
for c in range(0, n):
    from random import randint
    from time import sleep
    palpite = randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)
    lista.append(palpite)
    print(f'Jogo {c+1}: {palpite} ')
    sleep(1)
'''from random import sample
from time import sleep
n=int(input('Digite o números de palpites que deseja: '))
for d in range(0,n):
    for c in range(0,6):
        palpite=sample(range(1,61), 6)
    print(palpite)
    sleep(1)'''