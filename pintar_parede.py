# Informa a área da parede e quantos litros de tinta são necessários para pintar a parede por completo, sabendo que 1L de tinta pinta 2m^2 de parede
l = float(input('LARGURA (m): '))
h = float(input('ALTURA (m): '))
a = l*h
print('ÁREA: {:.2f} METROS QUADRADOS'.format(a))
print('QTD. TINTA: {:.2f}L'.format(a/2))
