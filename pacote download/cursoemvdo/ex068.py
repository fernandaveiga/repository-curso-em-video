# Faça um programa para jogar par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

print('Vamos jogar par ou ímpar!')
c=0
n=0
o=0
from random import randint
computador=randint(1,10)

while True:
    n=(int(input('Digite um valor: ')))
    o=str(input('Você quer par ou ímpar? [P ou I] ')).upper()
    if o=='P':
        if (computador+n)%2==0:
            print(f'Você ganhou! O computador jogou {computador} e você {n}, deu par')
            c=c+1
        else:
            print(f'Você perdeu! O computador jogou {computador} e você {n}, deu ímpar')
            break
    elif o=='I':
        if (computador+n)%2==1:
            print(f'Você ganhou! O computador jogou {computador} e você {n}, deu ímpar!')
            c=c+1
        else:
            print(f'Você perdeu! O computador jogou {computador} e você {n}, deu par!')
            break
print(f'Jogo terminado, você teve {c} vitórias')