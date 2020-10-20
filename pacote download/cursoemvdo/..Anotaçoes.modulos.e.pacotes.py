# Módulos são bibliotecas de fora do programa que contem funcionalidades que voce deseja usar no seu programa
# Abaixo está importado toda a biblioteca math, que contem raiz quadrada, seno, cosseno, tangente, arredonda
# números e muitas outras funcionalidades
# import math
# n = int(input('Digite um número: '))
# raiz = math.sqrt
# print(f'A raiz quadrada de {n} é igual a {raiz}')
# Abaixo importa a função raiz quadrada d biblioteca math
from math import sqrt#, floor (para importara mais de uma função da biblioteca, neste caso a arredondar pata baixo)
n = int(input('Digite um número: '))
raiz = (sqrt(n))
#raiz = floor(sqrt(n)) para a alternativa de usar o floor para arredondar para baixo
print(f'A raiz quadrada de {n} é igual a {raiz}')
# Para renomear uma função de um módulo
from math import floor as arredonda_baixo
a = float(input('Digite um número para arrendodar: '))
print(arredonda_baixo(a))