# Informa a ordem de apresentação dos alunos
from random import sample
aluno_1 = input('Primeiro aluno: ')
aluno_2 = input('Segundo aluno: ')
aluno_3 = input('Terceiro aluno: ')
aluno_4 = input('Quarto aluno: ')

alunos = [aluno_1,aluno_2,aluno_3,aluno_4]

print('A ordem de apresentação será')
print(sample(alunos, 4))