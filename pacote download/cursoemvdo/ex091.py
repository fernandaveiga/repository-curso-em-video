# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
# em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número
# no dado.
dicio = {}
lista = []
from random import randint
from time import sleep
for c in range(1, 5):
    r = randint(1, 6)
    dicio[f'jogador{c}'] = r
    print(f'O jogador{c} tirou {dicio[f"jogador{c}"]}')
    sleep(1)
    lista.append(dicio[f'jogador{c}'])
lista.sort(reverse=True)
print(lista)
print('-----RANKING-----')
for pos, item in enumerate(lista):
    print(f'{pos+1}º lugar: {item} pontos ')
    sleep(1)

'''dicio = {}
from random import randint
from time import sleep
from operator import itemgetter
for c in range(0,4):
    r = randint(1, 6)
    dicio[f'Jogador{c+1}'] = r
    print(f'O jogador {c+1} tirou {r}')
    sleep(1)
ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)
print(dicio)
print(ranking)
for pos, item in enumerate(ranking):
    print(f'{pos+1} lugar: {item[0]} com {item[1]}')'''
