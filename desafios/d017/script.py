print('====== DESAFIO 17 ======')
import math 

a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(a, b)
print(f'Se o valor do cateto oposto é {a} e o do cateto adjacente {b}, logo o comprimento da hipotenusa é {h:.2f}.')