'''Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

temperatura = float(input("Digite a temperatura que deseja converter: "))
unidade_origem = input("Digite a unidade de origem (Celsius, Fahrenheit, Kelvin): ")
unidade_destino = input("Digite a unidade de destino (Celsius, Fahrenheit, Kelvin): ")
if unidade_origem == "Celsius":
    if unidade_destino == "Fahrenheit":
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_destino == "Kelvin":
        temperatura_convertida = temperatura + 273.15
    else:
        temperatura_convertida = temperatura
if unidade_origem == "Fahrenheit":
    if unidade_destino == "Celsius":
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_destino == "Kelvin":
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
    else:
        temperatura_convertida = temperatura
if unidade_origem == "Kelvin":
    if unidade_destino == "Celsius":
        temperatura_convertida = temperatura - 273.15
    elif unidade_destino == "Fahrenheit":
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
    else:
        temperatura_convertida = temperatura
print(f"A temperatura convertida é: {temperatura_convertida:.2f} {unidade_destino}")

