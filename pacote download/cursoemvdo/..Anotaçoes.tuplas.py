# tuplas=() listas=[] e dicionarios = {}. Este caso é de TUPLAS
lanche=('Hamburguer', 'queijo', 'pao', 'maionese', 'bacon')

#sempre conta até um antes do ultimo número
print(lanche[:3])

#Paratodo c em lanche, some o c mais a string e alface
for c in lanche:
#for c in range(0,len(lanche)):
#   print(f'eu vou comer {lanche(c)} na posição {c}')
# para mostrar a posição
#ele não serve para este caso em que tem uma soma de strings
    print(f'Eu vou comer {c}')
    c=c+ ' e alface'
    print(c)
print('Gosto muito de alface...')

#Saber a quantidade de elementos na tupla lanche
print(len(lanche))

#sorted=muda a ordem, somente para mostrar essa vez
print(sorted(lanche))

a=(1,1,2,3)
b=(9,8,7,1)
d=a+b
print(d)
#contar quantas vezes tem o numero 1
print(d.count(1))
#Em qual posição teve a primeira aparição do 1
print(d.index(1))
#Em qual posição a partir da posição 1
print(d.index(1,2))
#deletar a tupla inteira
del(a)
print(a)