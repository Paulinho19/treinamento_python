# Informa a tabuada de multiplicação do valor apresentado de 0 à 10000
n1 = float(input('Informe o número '))
n2 = 0
resultados = {}
for i in range (10001):
    print('{:.0f} x {} = {:.2f}'.format(n1,n2,n1*n2))
    resultados[n2] = n1*n2
    n2+=1
print(resultados)