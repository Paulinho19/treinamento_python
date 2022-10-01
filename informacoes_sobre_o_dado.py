# Informa todas as informações técnicas ao usuário
analise = input('Digite o que será analisado: ')
print(type(analise))
print('Só letras? {}'.format(analise.isalpha()))
print('Só números? {}'.format(analise.isnumeric()))
print('Tem letras e números? {}'.format(analise.isalnum()))
print('Só tem espaços? {}'.format(analise.isspace()))