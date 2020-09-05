# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente
lista = []
lista2 = []
r='S'
while True:
    if r=='S':
        nome=str(input('Digite um nome: '))
        lista.append(nome)
        n1=float(input('Digite a primeira nota: '))
        lista.append(n1)
        n2=float(input('Digite a segunda nota: '))
        lista.append(n2)
        lista2.append(lista[:])
        lista.clear()
        r=str(input('Deseja adicionar mais nomes? [S/N]')).upper()
    elif r=='N':
        break
    else:
        r=str(input('Digite uma opção válida, S ou N: ')).upper()
print(lista2)
print(f' Nº    NOME    MÉDIA ')
for pos,item in enumerate(lista2):
    media=(lista2[pos][1]+lista2[pos][2])/2
    print(f'{pos:^4}{item[0]:^10}{media:^7}')
while True:
    s = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if s==999:
        break
    else:
        print(f'As notas da(o) {lista2[s][0]} são: [{lista2[s][1]}, {lista2[s][2]}] ')