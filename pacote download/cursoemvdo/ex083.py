# Crie um programa onde o usuário digite uma expressão qualquer que use parenteses. Seu aplicativo
# deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta

lista=list()
e=input('Digite uma expressão: ')
for pos, item in enumerate(e):
    lista.append(item)
    x=lista.count('(')
    y=lista.count(')')
if x==y:
    if x==y==0:
        print('Expressão válida.')
    elif lista.index('(')<lista.index(')'):
        print('Expressão válida')
    else:
        print('Expressão inválida')
else:
    print('Expressão inválida')
print(lista)