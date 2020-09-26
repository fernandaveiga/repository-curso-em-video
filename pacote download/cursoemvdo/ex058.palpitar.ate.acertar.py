# Melhore o jogo do DESAFIO 28 onde o computador vai pensar em um numero entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
# necessários para vencer

y=0
x=11
from random import randint
sorteado=randint(0,10)

while sorteado!=x:
    y=y+1
    x=int(input('Escolha um número de 0 a 10: '))
    if x>sorteado:
        print('Tente um numero menor!')
    if x<sorteado:
        print('Tente um numero maior!')
print(f'VOCÊ ACERTOU! O número escolhido por voce e pelo computador foi {sorteado} e o numero de tentativas até acertar foram {y}')