# Informa o valor de um produto em que foi aplicado 5% de desconto 
valor = float(input('VALOR DO PRODUTO R$'))
print('VALOR DO PRODUTO ATUALIZADO, COM 5% DE DESCONTO FICA: R${:.2f}'.format(valor-(valor*(5/100))))
