# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso
# lidos.

maior=0
menor=0
for p in range(1,6):
    peso=float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))

#maior=0
#menor=1000
#for n in range(1,6):
#    p = float(input('Digite o peso da {}ª pessoa: '.format(n)))
#    if p>maior:
#        maior=p
#    if p<menor:
#        menor=p
#print('''O maior é: {}
#O menor é: {}'''.format(maior, menor))