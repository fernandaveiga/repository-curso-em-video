# lista brasil
brasil =[]
# três dicionários
estado1 = {'nome': 'São Paulo', 'sigla': 'SP'}
estado2 = {'nome': 'Rio de Janeiro', 'sigla': 'RJ'}
estado3 = {'nome': 'Minas Gerais', 'sigla':'MG'}
# colocar os três dicionários em uma lista, na lista brasil
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
print(brasil)
# como brasil é uma lista, a posiçao zero é o primeiro dicionário adicionado
print(brasil[0])
# mostra o item 'sigla' da posição 1 da lista (neste caso o estado2)
print(brasil[1]['sigla'])
# deleta a chave sigla e o item do estado1 que é 'sigla ' e 'SP'
del estado1['sigla']
print(brasil)
