# o programa informa se o motorista será multado ou não
velocidade = float(input('Informe a velocidade do veículo: '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')