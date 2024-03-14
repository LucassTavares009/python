print('====== DESAFIO 29 ======')

km = float(input('Você estava digirindo a quantos Km/h? '))
limit = 80
if km > limit:
    excess = km - limit
    m = excess * 7
if km > 80:
    print(f'Você esta numa velocidade além da permitida, será multado!\n O valor da multa será R${m}.')
else:
    print('Você esta dirigindo na velocidade permitida, tenha um bom dia!')
