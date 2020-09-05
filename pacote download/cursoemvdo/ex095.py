# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador
dicio = {}
lista = []
lista2 = []
r = 'S'
while True:
    if r == 'S':
        dicio["nome"] = str(input('Nome do jogador: '))
        partidas = int(input(f'Partidas que o {dicio["nome"]} jogou: '))
        for c in range(0, partidas):
            gol = int(input(f'  Quantos gols na partida {c+1}? '))
            lista.append(gol)
            dicio['gol'] = lista[:]
            dicio['soma'] = sum(lista)
        lista2.append(dicio.copy())
        lista.clear()
        r = str(input('Deseja adicionar mais um jogador? ')).upper()[0]
    elif r == 'N':
        break
    else:
        r = str(input('Digite novamente, S ou N: ')).upper()[0]
print(lista2)
print('-=' * 20)
print('Cod nome          gols          total')
print('-' * 40)
for pos, item in enumerate(lista2):
    print(f'{pos:>3}', end = ' ')
    for v, k in item.items():
        print(f'{str(k):<14}', end = '')
    print()
while True:
    a = int(input('Deseja mostrar qual jogador? (999 para terminar)'))
    if a == 999:
        break
    if a >= len(lista2):
        print('Erro! Digite um código válido.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {lista2[a]["nome"]}: ')
        for pos, item in enumerate(lista2[a]["gol"]):
            print(f'==>Na partida {pos+1}, fez {item} gols')
        print(f'Num total de {lista2[a]["soma"]} gols')