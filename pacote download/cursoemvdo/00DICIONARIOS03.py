estado = {}
brasil = []
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
# coloca 3 dicionários contendo um UF e uma Sigla cada um
    brasil.append(estado.copy())
print(brasil)
# for para a lista, pra cada elemento da lista, neste caso, para cada dicionário
for e in brasil:
# for para o dicionário, com k sendo a chave e v o item de sua respectiva chave
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
# para mostrar os valores, os itens, ou seja, depois dos pontos do dicionário
#        print(v)
# para mostrar os valores, os itens de cada dicionário, sem espaço entre cada dois da chave
#        print(v, end='')
#    print()