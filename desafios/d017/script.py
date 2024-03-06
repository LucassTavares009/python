print('====== DESAFIO 17 ======')
from math import hypot

a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
h = hypot(a, b)
print(f'Se o valor do cateto oposto é {a} \ne o do cateto adjacente {b}, \nlogo o comprimento da hipotenusa é {h:.2f}.')