# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno

# com parametros globais
def area(larg, comp):
    area = larg * comp
    print(f'A área do terreno de largura {larg}m e comprimento {comp}m é igual a {area}m²')


print('Controle de terrenos')
print('-' * 20)
larg = float(input('Digite a largura: '))
comp = float(input('Digite o comprimento: '))
area(larg, comp)


'''# Sem parametro global, só local
def area():
    largura = float(input('Largura (m): '))
    comprimento = float(input('Comprimento (m): '))
    area = comprimento * largura
    print(f'A área do terreno {largura}x{comprimento} é igual a {area} m²')


area()'''
