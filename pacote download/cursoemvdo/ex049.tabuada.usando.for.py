# Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, só que agora
# utilizando um laço for

n = int(input('Digite um numero para a tabuada: '))
for c in range(1,11):
    x=c*n
    print('{} x {} = {}'.format(n,c,x))
#ou
#n = int(input('Digite um numero para a tabuada: '))
#for c in range(1,11):
#   print('{} x {} = {}'.format(num,c,num*c))