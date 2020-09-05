# Fatorial de um número
def fatorial(n):
    resp = 1
    for c in range(n, 0, -1):
        resp = resp*c
    return resp

#programa principal
num = int(input('Digite um número: '))
print(f'O fatorial de {num} é igual a {fatorial(num)}')

print('-'*32)
# Saber se é par ou não
def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
r = par(num)
if par(num)==True:
    print(f'É par!')
else:
    print('Não é par!')