# Escreva um programa para aprovar o emprestimo bancario para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar
# Calculo o valor da prestação mensal, sabendo que ela nao pode exceder 30%
# do salário ou então o emprestimo será negado

valorcasa=float(input('Digite o valor da casa que você irá comprar: '))
salario=float(input('Digite o valor do seu salário atual: '))
anos=float(input('Digite em quantos anos você deseja pagar a casa: '))

calcprest=valorcasa/(anos*12)
print('Se voce vai comprar uma casa que custa R${} em {} anos, pagará R${} fixos mensais.'.format(valorcasa, anos, calcprest))
if calcprest<=(0.3*salario):
    print('EMPRÉSTIMO APROVADO!! O valor a ser pago nas parcelas da casa nao excede 30% do seu atual salário.')
else:
    print('EMPRÉSTIMO NEGADO! O valor a ser pago pela casa excede 30% do seu salário.')
