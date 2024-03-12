print('====== DESAFIO 26 ======')

frase = str(input('Recite uma frase: ')).upper()
print(f"A letra 'A' aparece {frase.count('A')} vezes")
print(f"A letra 'A' aparece pela primeira vez na posição de número {frase.find('A')}")
print(f"A última vez que a letra 'A' aparece é na posição de número {frase.rfind('A')}")