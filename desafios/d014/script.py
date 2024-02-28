print('====== DESAFIO 14 ======')

print('CONVERSOR DE TEMPERATURAS')

celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15
print(f'{celsius}°C é equivalente a {fahrenheit}°F.')
print(f'{celsius}°C é equivalente a {kelvin}°K.')
