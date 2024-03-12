print('====== DESAFIO 24 ======')

city = str(input('Diga o nome da sua cidade: ')).upper().split()
if 'SANTO' in city[0]:
    print('Sua cidade começa com santos.')
else:
    print('Sua cidade não começa com santos.')