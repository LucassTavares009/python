print('====== DESAFIO 15 ======')

print('ALUGUEL DE CARROS')

km = float(input('Quantos Km você percorreu com o carro? '))
d = int(input('Você alugou o carro por quantos dias? '))
p = (d * 60.00) + (km * 0.15)
print(f'Você percorreu {km}Km e alugou o carro por {d} dias, o total a pagar é: R${p:.2f}')
