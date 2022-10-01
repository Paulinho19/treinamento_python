# Informa ao usuário a conversão de uma temperatura de Celsius para Fahrenheit
temperatura = float(input('INFORME A TEMPERATURA EM C°: '))
print('A TEMPERATURA {:.2f}°C CONVERTIDO EM FAHRENHEIT FICA: {:.2f}°F'.format(temperatura,32+(temperatura*(9/5))))