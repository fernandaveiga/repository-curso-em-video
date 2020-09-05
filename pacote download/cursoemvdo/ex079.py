# Crie um programa onde o usuário possa digitar
# valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem
# crescente

lista=list()
r='S'
while r=='S':
    n= int(input('Digite um número para a lista: '))
    if n in lista:
        print('Este número não será adicionado..')
        n=int(input('Digite outro número: '))
        if n not in lista:
            lista.append(n)
            print('Número adicionado com sucesso..')
        print('Este número não será adicionado')
    else:
        lista.append(n)
        print('Número adicionado com sucesso..')
    r=str(input('Deseja digitar mais um número? [S/N]')).upper()
    if r!='S' and r!='N':
        r=str(input('Digite uma opção válida, S ou N : ')).upper()
print(sorted(lista))

#ou
'''lista=[]
r='S'
while r=='S':
    n=int(input('Digite um número: '))
    while n in lista:
        print('Este número não será adicionado...')
        n=int(input('Digite outro número: '))
    lista.append(n)
    print('Número adicionado com sucesso!')
    r=str(input('Deseja continuar a adicionar números? [S/N]')).upper()
    if r!='S' and r!='N':
        r=str(input('Digite uma opção válida, S ou N: ')).upper()
print(f'A lista em ordem crescente é {sorted(lista)}')'''