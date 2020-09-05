# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais

tupla=('aveia', 'ovo', 'quinoa', 'chia', 'granola', 'linhaça', 'floco de arroz', 'amaranto', 'arroz negro',
          'grao de bico', 'lentinha', 'ervilha', 'linhaça dourada')

for palavra in tupla:
    print(f'\nA palavra {palavra.upper()} tem a(s) vogal(is) ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')