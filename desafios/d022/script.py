print('====== DESAFIO 22 ======')

name = str(input('Qual o seu nome completo: '))
print(f'Seu nome em maiúsculo é {name.upper()}')
print(f'Seu nome em minúsculo é {name.lower()}')
print(f'O seu nome tem ao todo {len(name.strip()) - name.count(' ')} letras')
dividido = name.split()
print(f'O primeiro nome é {dividido[0]} e tem {len(dividido[0])} letras.')
