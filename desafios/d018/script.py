print('====== DESAFIO 18 ======')

from math import radians, sin, cos, tan 

a_graus =(int(input('Diga o ângulo: ')))
a = radians(a_graus)
s = sin(a)
c = cos(a)
t = tan(a)
print(f'Se o ângulo é {a_graus}, \nlogo o valor do seno é {s:.2f}, \no valor do cosseno {c:.2f} \ne o valor da tangente {t:.2f}.')