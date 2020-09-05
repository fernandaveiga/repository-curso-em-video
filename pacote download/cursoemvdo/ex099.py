# Faça um programa que tenha uma funçao maior(), que receba vários parametros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior
# (adicionei para contar a quantidade da lista, mostrar a lista e falar qual o menor número)
# Faça um programa que tenha uma funçao maior(), que receba vários parametros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior

def maior(*n):
    from time import sleep
    maior = 0
    menor = 0
    for pos, item in enumerate(n):
        if pos == 0:
            maior = item
            menor = item
        else:
            if item > maior:
                maior = item
            if item < menor:
                menor = item
    print(f'Analisando os valores passados...')
    sleep(0.5)
    for c in n:
        print(f'{c}', end = ' ')
        sleep(0.5)
    print()
    print(f'A lista tem {pos+1} itens')
    sleep(0.5)
    print(f'O maior valor é o {maior}')
    sleep(0.5)
    print(f'O menor valor é o {menor}')
    sleep(0.5)
    print('-'*32)


maior(8, 1, 9, 6, 2, 7)
maior(7, 2, 9)
maior(1, 8, 99, 0, 13, 2)
maior(1, 7)
maior(7)

