def fatorial(n):
    f = 1
    for c in range(1, n+1, 1):
        f = f*c
    return f

n = int(input('Digite um número para o calculo do fatorial: '))
fat = fatorial(n)
print(f'O fatorial de {n} é igual a {fat}')