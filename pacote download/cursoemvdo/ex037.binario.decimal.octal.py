# Escreva um programa que leia um numero inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão
# 1 para binario
# 2 para octal
# 3 para hexadecimal

num=int(input('Digite um numero inteiro: '))
op=int(input('''Digite o numero correspondente à conversão que deseja fazer:
[1] Binário
[2] Octal
[3] Hexadecimal '''))
if op==1:
    print('O numero digitado foi {} e convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif op==2:
    print('O numero digitado foi {} e convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif op==3:
    print('O numero digitado foi {} e convertido para binário é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Você não digitou uma opção válida')