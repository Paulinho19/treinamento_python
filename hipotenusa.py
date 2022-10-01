# informa o comprimento da hipotenusa
from math import sqrt 
cateto_oposto = float(input('Comprimento do cateto oposto (m): '))
cateto_adjacente = float(input('Comprimento do cateto adjacente (m): '))
print('A hipotenusa vai medir: {:.2f}m'.format(sqrt((pow(cateto_oposto, 2)) + (pow(cateto_adjacente, 2)))))