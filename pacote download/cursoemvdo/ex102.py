# Crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro
# que indique o número a calcular e o outro chamado show, que sera um valor lógico(opcional)
# indicando se será mostrado ou não na tela o processo de calculo fatorial

def fatorial(numero, show = False):
    '''
    Calcula o fatorial de um número digitado
    :param numero: Número que será calculado o fatorial
    :param show: Se true, mostra o calculo do fatorial, se false, mostra apenas o resultado
    :return: o valor do fatorial de n
    '''
    if show == False:
        resp = 1
        for c in range(n, 0, -1):
            resp = resp*c
        print(f'A resposta do fatorial é igual a {resp}')
    if show == True:
        resp = 1
        for c in range(n, 0, -1):
            resp = resp*c
            if c != 1:
                print(f'{c}x', end='')
            if c == 1:
                print(f'{c}={resp}')


n = int(input('Número para calculo do fatorial: '))
fatorial(n, True)
help(fatorial)


