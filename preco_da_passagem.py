# O program informa qual o valor que o usuário irá pagar em uma passagem
distancia = float(input('Informe a distância da viagem em km: '))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Você está prestes a viajar uma distância de {:.2f}km'.format(distancia))
print('O valor da passagem é: R${:.2f}'.format(preco))