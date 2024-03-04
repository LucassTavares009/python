n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A some é {a}, \no produto é {m} e a \ndivisão é {d:.3f}.', end=' ')
print(f'\nDivisão intera {di} \ne potência {e}.')