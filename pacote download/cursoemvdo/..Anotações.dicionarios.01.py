# as keys, o que ta escrito antes dos dois pontos, equivale a posição do item,
# que é o que ta dentro do grupo, o item
pessoas = {'nome': 'Amanda', 'Sexo': 'F', 'idade': 27}
# Em listas, para mostrar uma posição específica usava-se lista[pos]. Em dicionários, as posições são nomes
print(pessoas['idade'])
# Aspas duplas dentro do colchete
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
# para mostrar os nomes de chaves, neste caso sendo nome, sexo e idade
print(pessoas.keys())
# para mostrar os valores das chaves, neste caso amanda, F e 27
print(pessoas.values())
# para mostrar cada item que é referente a cada grupo de informações
print(pessoas.items())
# para mostrar cada item dentro das chaves, com quebra de linha entre cada um
for k in pessoas.values():
    print(k)
# para mostrar os nomes de chaves, antes dos dois pontos, com quebra de linha
for k in pessoas.keys():
    print(k)
# pos é a posição no dicionário, que equivale ao nome de chave. O item é o que vem dentro do grupo,
# depois dos dois pontos
for pos, item in pessoas.items():
    print(f'{pos}-> {item}')
# Quando voce exclui uma chave, o item da chave também é excluído
del pessoas['idade']
print(pessoas)
# para trocar um item de alguma chave
pessoas['nome'] = 'luri'
# para adicionar uma chave e um item
pessoas['peso'] = 60
