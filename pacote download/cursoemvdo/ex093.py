# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
# o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
# em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de
# gols feitos durante o campeonato
dicio = {}
lista  = []
dicio["nome"] = str(input('Nome do jogador: '))
partidas = int(input(f'Partidas jogadas pelo {dicio["nome"]}: '))
for c in range(0, partidas):
    gol = int(input(f'  Quantos gols na partida {c+1}? '))
    lista.append(gol)
    dicio['gol'] = lista[:]
    dicio["soma"] = sum(lista)
print(dicio)
for k, v in dicio.items():
    print(f'O campo {k} tem valor {v} ')
print(f'O jogador {dicio["nome"]} jogou {partidas} partidas: ')
for pos, item in enumerate(lista):
    print(f'==>Na partida {pos}, fez {item} gols')
print(f'Num total de {dicio["soma"]} gols')
