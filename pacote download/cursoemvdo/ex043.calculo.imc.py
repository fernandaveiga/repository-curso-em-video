# desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# e acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# entre 18.5 e 25: Peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade morbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc=peso/(altura**2)

if imc<18.5:
    print('Você está abaixo do seu peso ideal e seu imc={}.'.format(imc))
elif 18.5<=imc<25:
    print('Você está dentro do seu peso ideal e seu imc={}.'.format(imc))
elif 25<=imc<30:
    print('Você está com sobrepeso e seu imc={}'.format(imc))
elif 30<=imc<40:
    print('Você está com obesidade e seu imc={}'.format(imc))
else:
    print('Você está com obesidade morbida e seu imc={}'.format(imc))