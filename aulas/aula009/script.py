frase = 'Curso em Vídeo Python'
# fatiamento de string:
print(frase[3])
print(frase[3:13])
print(frase[3:13:2])
print(frase[:3])
print(frase[3:])

# Imprimindo textos inteiros:

print(''''Não importa o mundo, não, só minha ambição
Haki do Rei?
É o mínimo que eu esperava do Capitão
Atrás de minhas dores não vou me esconder
Vão ver
Se uma ferida mata um homem comum
Um homem comum então eu não posso ser!''')

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'JavaScript'))
print('Python' in frase)
print(frase.find('Python'))
print(frase.find('python'))
print(frase.lower().find('python'))
print(frase.split())

dividido = frase.split()
print(dividido[0])
print(dividido[2] [3])
