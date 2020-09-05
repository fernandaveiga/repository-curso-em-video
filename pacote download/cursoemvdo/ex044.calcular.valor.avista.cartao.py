# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# à vista no dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

p=float(input('Qual é o valor normal do produto? '))
pt=int(input('''Digite o numero equivalente a forma de pagamento: 
1 para à vista no dinheiro/cheque, 
2 para à vista no cartão, 
3 para até 2x no cartão e 
4 para 3 ou mais vezes no cartão: '''))

if pt==1:
    pf=p*0.9
    print('O valor do produto que custa {} vai ficar {}'.format(p,pf))
elif pt==2:
    pf=p*0.95
    print('O valor do produto que custa {} vai ficar {}'.format(p,pf))
elif pt==3:
    pf=p
    print('O valor do produto ficará em seu preço total normal de {}'.format(pf))
elif pt==4:
    pf=p*1.2
    print('O valor do produto que custa {} vai ficar com preço total igual a {}'.format(p,pf))
else:
    print('Você nao digitou uma opção válida. Digite um numero de 1 a 4.')