# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico

def leiaint(msg):
    n = input(msg)
    while True:
        if n.isnumeric():
            return n
        else:
            print('ERRO! Digite um número inteiro. ')
            n = input(msg)


n = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número inteiro {n}')