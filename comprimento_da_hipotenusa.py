# Informa o valor que a hipotenusa terá
import math
cateto_oposto = float(input('CATETO OPOSTO (m): '))
cateto_adjacente = float(input('CATETO ADJACENTE (m): '))
print('HIPOTENUSA VALE (m): {:.2f}'.format(math.sqrt((pow(cateto_oposto,2))+(pow(cateto_adjacente,2)))))