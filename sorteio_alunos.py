# Apresenta o nome do aluno que foi sorteado para apagar o quadro
import random
alunos = {}
for i in range(4):
    nome_aluno = input('NOME DO ALUNO: ')
    alunos[i] = nome_aluno
print()
print('O ALUNO ESCOLHIDO PARA APAGAR O QUADRO FOI: {}'.format(alunos[random.randint(0,3)].upper()))
