# Interactive help:
# Docstrings
# Argumentos opcionais
# Escopo de variáveis
# Retorno de variáveis

# *** INTERACTIVE HELP ***
# Ajuda interativa sobre os comandos do python, é como um manual do comando que voce deseja saber mais.
# Você pode escrever help() no console, ou: help(comandodesejado), exemplo:
help(print)
# ou
print(input.__doc__)

# *** DOCSTRINGS ***
# Manual do def comando que voce criou
# Quando você monta a sua ajuda em funções. Após o comando def, voce abre aspas duplas três vezes e
# o python vai abrir um local em verde para que voce escreva o que deseja colocar no help(area),
# como no exemplo a seguir. Se voce não colocar as tres aspas duplas, quando voce colocar help(area)
# não obterá um help consistente, pois foi você criou o comando area, nao o computador. Voce cria o
# comando e precisa criar o manual deste comando que você criou
def area(larg, comp):
    """

    :param larg:
    :param comp:
    :return:
    """
    area = larg * comp
    print(f'A área do terreno de largura {larg}m e comprimento {comp}m é igual a {area}m²')


help(area)

# *** ARGUMENTOS OPCIONAIS ***
# Você pode colocar uma opção alternativa para os parametros. No exemplo abaixo, você percebe que se ao
# chamar a função somar, não haver qualquer um dos três parametros, o parametro que nao for chamado
# receberá 0. Pode colocar como parametro opcional os tres parametros, ou só um deles
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 4)
somar(8, 4)

# *** ESCOPO DE VARIÁVEIS ***
# Uma variável que é criada dentro do defcomando só vale dentro do defcomando, é chamada de variável local.
# Não pode ser chamada num print fora do defcomando. Fora do defcomando pode haver, inclusive, uma variável
# com o mesmo nome de uma variável local e não poderá ser chamada dentro do defcomando. A variável com o
# mesmo nome e fora do defcomando só poderá ser chamada num print fora do defcomando. Exemplo:
def teste(b):
# Para usar o parametro a global e não o local deve colocar:
    #global a
    a = 8
    b = b + 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')

# *** RETORNO DE VALORES ***
def soma(a = 0, b = 0, c = 0):
    s = a + b + c
    r = s * a
    return r


x = soma(2, 5, 3)
y = soma(7, 1)
z = soma(6)
print(f'Meus calculos deram {x}, {y} e {z}')
# outra forma de fazer que tambem da certo
#print(f'Os meus calculos deram ', end='')
#print(soma(3,2,5), end=', ')
#print(soma(7,1), end=' e ')
#print(soma(6))
#r1 = soma(3, 2, 5)
#r2 = soma(1, 7)
#r3 = soma(4)
#print(f'Meus calculos deram {r1}, {r2} e {r3}.')


