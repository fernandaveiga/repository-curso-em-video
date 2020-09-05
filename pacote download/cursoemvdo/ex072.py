t=('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
   'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
   'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS',
   'DEZESSTE', 'DEZOITO', 'DEZENOVE', 'VINTE')

r='S'
while r=='S':
    n = int(input('Digite um número de 0 a 20: '))
    while n<0 or n>20:
        n=int(input('Você não digitou um número válido. Digite novamente, entre 0 e 20: '))
    print(f'Você digitou o número {t[n]}!')
    r = str(input('Você deseja continuar? Digite S para sim ou N para não:  ')).upper()
print('FINISHED')

'''t=('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
   'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
   'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS',
   'DEZESSTE', 'DEZOITO', 'DEZENOVE', 'VINTE')

while True:
    n=int(input('Digite um número entre 0 e 20: '))
    if 0<= n<=20:
        break
    print('Tente novamente.', end='')
print(f'Você digitou o número {t[n]}')'''

