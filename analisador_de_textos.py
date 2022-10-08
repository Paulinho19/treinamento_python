# Apresenta o nome de diferentes formas e algumas informações da string
nome = str(input('Digite seu nome completo: '))
primeiro_nome = nome.split(' ')
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em maiúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ',''))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro_nome[0],len(primeiro_nome[0])))

