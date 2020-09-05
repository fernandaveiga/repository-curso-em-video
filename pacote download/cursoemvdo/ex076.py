# Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular

lista=('hamburguer', 20, 'pao', 5, 'queijo', 5,
   'maionese', 3, 'bacon', 7, 'maionese verde', 4)

print('-'*40)
print(F'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for posicao in range(0,len(lista)):
    if posicao%2==0:
        print(f'{lista[posicao]:.<30}', end='')
    else:
        print(f'R${lista[posicao]:.>8.2f}')
