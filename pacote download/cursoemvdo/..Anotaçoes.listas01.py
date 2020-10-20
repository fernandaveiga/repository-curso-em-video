lanche=['pao', 'hamburguer', 'alface',
        'bacon', 'maionese']
# comando para adicionar um elemento ao final da lista
lanche.append('queijo')
print(lanche)
# comando para adicionar um elemento em alguma
# posição específica
lanche.insert(0,'maionese verde')
print(lanche)
# comando para deletar um item pela chave
del lanche[3]
print(lanche)
# o comando pop serve para deletar tambem, e sem um numero dentro
# do colchete, serve para deletar o último elemento da lista
lanche.pop(0)
print(lanche)
# Para remover um item pelo nome/elemento
lanche.remove('bacon')
print(lanche)
# Se tentar remover um elemento que não existe na lista
# dá erro. se nao souber se o elemento ainda está na lista:
if 'bacon' in lanche:
    lanche.remove('bacon')
# criar uma lista com range
valores1 = list(range(4, 11))
print(valores1)
#ordenar uma lista
valores2 = [7, 3, 9, 8, 1, 6, 6, 2]
valores2.sort()
print(valores2)
#ordenar uma lista ao contrário
valores2.sort(reverse=True)
print(valores2)
# Saber o tamanho da lista
print(len(valores2))

