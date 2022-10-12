# Informa a tabuada de multiplicação do valor apresentado de 0 à 10000
continua = 's'
while continua == 's':
    n1 = float(input('Informe o número: '))
    n2 = 0
    for i in range (201):
        print('{} x {} = {:.2f}'.format(n1,n2,n1*n2))
        n2+=1
    print()
    continua = input('Deseja continuar (s/n): ')
