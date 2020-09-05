# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
# dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação
# e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
from datetime import datetime
dicio = {}
dicio['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dicio['cart'] = int(input('N da carteira de trabalho: '))
dicio['idade'] = datetime.now().year - nasc
if dicio['cart'] != 0:
    dicio['anoc'] = int(input('Ano de contratação: '))
    dicio['salario'] = float(input('Digite o salário: '))
    dicio['aposent'] = (dicio['anoc'] +35) - nasc
    print(f'Nome tem valor {dicio["nome"]}'
          f'\n Idade tem valor {dicio["idade"]}'
          f'\n Carteira de trabalho tem valor {dicio["cart"]}'
          f'\n Contratação teve ano {dicio["anoc"]}'
          f'\n Salário tem valor {dicio["salario"]}'
          f'\n Aposentadoria tem valor {dicio["aposent"]}')
else:
    print(f'O nome tem valor {dicio["nome"]}'
          f'\nIdade tem valor {dicio["idade"]}'
          f'\nCarteira de trabalho tem valor {dicio["cart"]}')
print(dicio)