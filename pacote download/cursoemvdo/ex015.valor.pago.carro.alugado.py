t=int(input('Digite quantos dias voce utilizou o carro alugado: '))
d=float(input('Digite a quantidade de quilometros que o carro percorreu no período utilizado: '))

valor=(t*60)+(0.15*d)

print('O valor a ser pago na quantidade de {} dias e {}km é igual a R${}'.format(t,d,valor))