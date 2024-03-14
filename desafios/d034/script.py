print('====== DESAFIO 34 ======')

sall = float(input('Qual o seu salário? '))
if sall > 1250:
    new = sall + (sall * 0.10)
else:
    new = sall + (sall * 0.15)
print(f'Seu novo salário é: {new}')