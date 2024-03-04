print('====== DESAFIO 18 ======')

import math

a_graus =(int(input('Diga o ângulo: ')))
a = math.radians(a_graus)
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print(f'Se o ângulo é {a_graus}, \nlogo o valor do seno é {s:.3f}, \no valor do cosseno {c:.3f} \ne o valor da tangente {t:.3f}.')