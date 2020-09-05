# Escreva um programa que leia o salário de um funcionário
# e calcule o valor de seu aumento
# Para salários superiores a R$1.200,00, calcule um aumento de 10%
# Para salários iguais ou inferiores a isso, calcule um aumento de 15%

salario=float(input('Qual o salário do funcionário? '))

if salario>1200:
    salario2=salario*1.1
    print('O salário atual é R${} e com aumento de 10% ficará R${}.'.format(salario, salario2))
else:
    salario2=salario*1.15
    print('O salário atual é R${} e com o aumento de 15% ficará R${}.'.format(salario, salario2))