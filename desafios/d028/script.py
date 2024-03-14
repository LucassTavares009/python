print('====== DESAFIO 28 ======')

from random import choice
num = int(input('Digite um número: '))
ul = [0, 1, 2, 3, 4, 5]
lucky = choice(ul)
print(f'O número sorteado foi {lucky}')
if num == lucky:
    print('Que sorte! Você venceu!')
else: 
    print('Que pena, você perdeu!')