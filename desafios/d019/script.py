print('====== DESAFIO 19 ======')

from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
names = [n1, n2, n3, n4]
ul = choice(names)
print(f'O aluno que apagará a lousa será o: {ul}.')
