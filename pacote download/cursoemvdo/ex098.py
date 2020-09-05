# Faça um programa que tenha a função chamada contador(), que receba três parametros: inicio, fim e passo e
# realize a contagem. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
def personalize(i, f, p):
    from time import sleep
    print(f'A contagem de {i} a {f} de {p} em {p}:')
    if i < f:
        if p > 0:
            for c in range(i, f+1, p):
                print(f'{c}', end=' ')
                sleep(0.5)
        if p < 0:
            for c in range(i, f+1, -p):
                print(f'{c}', end=' ')
    elif i > f:
        if p > 0:
            for c in range(i, f-1, -p):
                print(f'{c}', end=' ')
                sleep(0.5)
        if p < 0:
            for c in range(i, f-1, p):
                print(f'{c}', end=' ')
                sleep(0.5)
    else:
        print(f'ERRO! O inicio e o fim tem valor igual {i} = {f}')
    print()


personalize(1, 10, 1)
personalize(10, 0, 2)

print('Agora é sua vez de personalizar a contagem: ')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

if p != 0:
    personalize(i, f, p)
else:
    personalize(i, f, 1)

