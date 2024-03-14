#estrutura condicional simplificada
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi: {m:.1f}')
print(f'REPROVADO!'if m < 5 else 'APROVADO!')