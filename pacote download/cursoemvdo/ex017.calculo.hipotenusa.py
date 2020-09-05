c01=float(input('Digite um primeiro cateto do triângulo: '))
c02=float(input('Digite o outro cateto do triângulo: '))

from math import hypot

h=hypot(c01,c02)

print('A hipotenusa correspondente ao triângulo de catetos {} e {} é igual a {}'.format(c01,c02,h))
