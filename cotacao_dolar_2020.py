# Informa quantos dólares podem ser adiquiridos com o valor que o usuário tem na carteira
n = float(input('Informe quantos reais você possui '))
if n//3.27 == 0:
    print('VOCÊ NÃO CONSEGUE COMPRAR NENHUM DÓLAR COM ESTE VALOR')
else:
    print('VOCÊ PODE COMPRAR {:.2f} DÓLARES'.format(n//3.27))