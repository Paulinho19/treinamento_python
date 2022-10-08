# informa se o nome da cidade se inicia com "SANTO"
cidade = str(input('Em qual cidade você nasceu? ')).strip().upper()
print(cidade[:5]  == 'SANTO')