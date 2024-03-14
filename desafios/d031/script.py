print('====== DESAFIO 31 ======')

km = float(input('Qual a distância da viagem em Km? '))
pass_price = km * 0.50
long_travel = km * 0.45

if km <= 200:
    print(f'Você viajou {km} Km, logo o preço da passagem será:R${pass_price:.2f}')
else: 
    print(f'Você viajou {km} Km, logo o preço da passagem será:R${long_travel:.2f}')