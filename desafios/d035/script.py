print('====== DESAFIO 35 ======')

r1 = float(input('Diga o comprimento da primeira reta: '))
r2 = float(input('Diga o comprimento da segunda reta: '))
r3 = float(input('Diga o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com essa medidas é possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo com essas medidas.')
