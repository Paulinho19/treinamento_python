# Informa ao usuário as informações de um número digitado
numero = str(input('Informe um número: '))
if len(numero) == 1:
    print('Unidade: {}'.format(numero[0]))
    print('Dezena: 0')
    print('Centena: 0')
    print('Milhar: 0')

elif len(numero) == 2:
    print('Unidade: {}'.format(numero[-1]))
    print('Dezena: {}'.format(numero[0]))
    print('Centena: 0')
    print('Milhar: 0')

elif len(numero) == 3:
    print('Unidade: {}'.format(numero[-1]))
    print('Dezena: {}'.format(numero[1]))
    print('Centena: {}'.format(numero[0]))
    print('Milhar: 0')

elif len(numero) == 4:
    print('Unidade: {}'.format(numero[-1]))
    print('Dezena: {}'.format(numero[2]))
    print('Centena: {}'.format(numero[1]))
    print('Milhar: {}'.format(numero[0]))

    
    
         
 
    
    