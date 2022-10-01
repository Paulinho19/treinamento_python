# Informa o valor que o cliente deverá pagar ao devolver o carro alugado
dias = int(input('Informe quantos dias em que utilizou o carro: '))
distancia = float(input('Informe quantos quilômetros o veículo percorreu: '))
print('-'*24)
print('Valor a pagar: R${:.2f}'.format((dias * 60) + (distancia * 0.15)))
print('-'*24)