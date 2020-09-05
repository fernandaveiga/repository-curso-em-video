#Crie um programa que leia dois valores e mostre um menu na tela
#[1] somar
#[2] multiplicar
#[3]maior
#[4]novos numeros
#[5]sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso

x=int(input('Digite um valor: '))
y=int(input('Digite outro valor: '))
op=0

while op!=5:
    op = int(input('''Digite a opção desejada para:
    [1] somar
    [2] multiplicar
    [3] Saber o maior valor
    [4] novos numeros
    [5] sair do programa '''))
    if op>0 and op<5:
        if op==1:
            z=x+y
            print('A soma é igual a {}'.format(z))
        elif op==2:
            w=x*y
            print('A multiplicação é igual a {}'.format(w))
        elif op==3:
            if x>y:
                print('O primeiro valor que é {} é maior que o segundo'.format(x))
            elif y>x:
                print('O segundo valor é {} e é maior que o primeiro'.format(y))
            else:
                print(' Os dois valores são iguais.')
        elif op==4:
            x=int(input('Digite outro valor: '))
            y=int(input('Digite mais um outro valor: '))
    elif op==5:
        print('SAIU DO PROGRAMA')
    else:
        print('digite uma opção válida')
print('ACABOU')