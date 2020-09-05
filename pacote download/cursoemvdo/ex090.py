# Faça um programa que leia nome e média de um aluno, guardando também a situação deste aluno em um
# dicionário. No final, mostre o conteúdo da estrutura na tela
dicio = {}

dicio['nome'] = str(input('Nome do aluno: '))
dicio['media'] = float(input('Média do(a) aluno(a): '))
if dicio['media']>=0 and dicio['media']<4:
    dicio['situacao'] = 'Reprovado'
elif dicio['media']>=4 and dicio['media']<6:
    dicio['situacao'] = 'Recuperação'
else:
    dicio['situacao'] = 'Aprovado'
for k, v in dicio.items():
    print(f'{k} é igual a {v}')