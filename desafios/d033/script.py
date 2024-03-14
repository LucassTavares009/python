print('====== DESAFIO 33 ======')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
#verificando o num1
if num1 < num2 and num1 < num3:
    print(f'O número {num1} é o menor')
if num1 > num2 and num1 > num3:
    print(f'O número {num1} é o maior')

#verificando o num2
if num2 < num1 and num2 < num3:
    print(f'O numéro {num2} é o menor.')
if num2 > num1 and num2 > num3:
    print(f'O número {num2} é o maior.')

#verificando o num3
if num3 < num2 and num3 < num1:
    print(f'O número {num3} é o menor.')
if num3 > num2 and num3 > num1:
    print(f'O número {num3} é o maior.')

