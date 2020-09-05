# Crie  uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato
# brasileiro de futebol, na ordem de colocação. Depois mostre:
#a) apenas os 5 primeiros colocados
#b) os ultimos 4 colocados a tabela
#c) Uma lista com os times em ordem alfabética
#d) em que posição na tabela está o time da bragantino

times=('São Paulo', 'Palmeiras', 'Atlético Mineiro', 'Vasco', 'Fluminense', 'Bragantino', 'Londrina', 'Botafogo',
       'Corinthians', 'Santos', 'Vasco', 'Athlético Paranaense', 'Goiás', 'Internacional', 'Coritiba', 'Bahia',
       'Manaus', 'Atlético de Goiás', 'Fortaleza', 'Gremio')
c=0
print(f'Os cinco primeiros colocados no campeonato são {times[0:5]}.')
print(f'Os quatro ultimos colocados são {times[16:20]}')
print(f'Os times do campeonato em ordem alfabética são {sorted(times)}')
print('O time Bragantino está na posição {}'.format(times.index('Bragantino')+1))
print('A classificação ficou: ')
for time in times:
    c=c+1
    print(f'{c}º {time}')
#a letra c do exercício pode ser feito assim:
'''for pos, time in enumerate(t):
    if time=='BRAGANTINO':
        print(f'O time {time}, está na posição {pos+1}')'''