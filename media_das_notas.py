# Informa a média do usuário baseada em duas notas apresentadas
n1,n2 = input('Informe as notas: ').split()
n1,n2 = float(n1), float(n2)
print('Média {:.2f}'.format((n1+n2)/2))