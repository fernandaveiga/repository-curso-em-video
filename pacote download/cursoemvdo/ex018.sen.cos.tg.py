from math import (radians,sin,cos,tan)

a=float(input('Digite um âlgulo: '))

sen=sin(radians(a))
cos=cos(radians(a))
tang=tan(radians(a))

print('O ângulo digitado é {}, seu seno igual a {}, cosseno igual a {} e tangente igual a {}'.format(a,sen,cos,tang))