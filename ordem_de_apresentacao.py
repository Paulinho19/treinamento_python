# O programa informa a ordem de apresentação dos alunos
# Apresenta o nome do aluno que foi sorteado para apagar o quadro
import random
alunos = {}
for i in range(4):
    nome_aluno = input('NOME DO ALUNO: ')
    alunos[i] = nome_aluno

for e in range(4):
    
    sorteado = alunos[random.randint(0,3)]
    print('APRESENTAÇÃO {}: {}'.format(e+1, sorteado.upper()))
#print('O ALUNO ESCOLHIDO PARA APAGAR O QUADRO FOI: {}'.format(alunos[random.randint(0,3)].upper()))
