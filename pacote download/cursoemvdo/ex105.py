# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionario com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicione também as docstrings da função

def notas(*n, sit = False):
    '''

    :param n: n equivale aos valores das notas
    :param sit: situação equivale a se o aluno está aprovado, reprovado ou
    precisa fazer o exame da disciplica. É OPCIONAL
    :return: retorna valores de maior e menor valor, média e situação
    '''
    dicio = {}
    maior = 0
    menor = 0
    soma = 0
    c = 0
    for pos, item in enumerate(n):
        soma = soma + item
        c = c + 1
        if pos == 0:
            maior = item
            menor = item
        else:
            if item > maior:
                maior = item
            if item < menor:
                menor = item
    print(f'O maior valor é {maior}')
    print(f'O menor valor é {menor}')
    media = soma / c
    print(f'A média é igual a {media}')
    dicio['maior_valor'] = maior
    dicio['menor_valor'] = menor
    dicio['media'] = media
    if sit==True:
        if media>=7 and media<=10:
            dicio['sit']='situacao_APROVADO'
        elif media<7 and media>=5:
            dicio['sit']='situaco_EXAME'
        elif media<5 and media>=0:
            dicio['sit']='situacao_REPROVADO'
    print(dicio)



notas(6, 7.9, 3, 2, sit=False)
notas(3, 7, 2, 2.5, sit=True)
notas(2.5, 7, 5, 2.5, sit=True)

'''def notas(*n, sit=False):
    dicio = {}
    dicio['total'] = len(n)
    dicio['maior'] = max(n)
    dicio['menor'] = min(n)
    dicio['media'] = sum(n)/len(n)
    if sit == True:
        if dicio['media']>=7:
            dicio['situação'] = 'BOA'
        elif dicio['media'] >= 5:
            dicio['situação'] = 'RAZOÀVEL'
        else:
            dicio['situação'] = 'RUIM'
    return dicio


notas(3, 7, 5.5, 2.5, sit=True)
notas(9, 6, 5, sit=False)'''