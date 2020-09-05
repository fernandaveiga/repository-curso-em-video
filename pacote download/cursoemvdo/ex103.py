# Faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: o nome de
# um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
# corretamente

'''def ficha(nome, gols=0):
    if nome == '' and gols == '':
        print(f'O jogador <desconhecido> fez 0 gols')
    elif gols == '':
        print(f'O jogador {nome} fez 0 gols. ')
    elif nome =='' :
        print(f'O jogador tem nome <desconhecido> fez {gols} gols')
    else:
        print(f'O jogador {nome} fez {gols} gols.')


n = (input('Nome do jogador: '))
gol = (input('Número de gols que o jogador fez: '))
ficha(n, gol)'''

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato')


# programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() =='':
    ficha(gol=g)
else:
    ficha(n,g)