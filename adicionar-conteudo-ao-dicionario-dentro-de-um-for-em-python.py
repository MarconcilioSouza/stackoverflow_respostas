import pandas as pd
from IPython.display import display

alunos = []

total_alunas_sala = int(input('Quantos alunos há na sala ? '))

for c in range(1, total_alunas_sala+1):
  nome = input(f'Qual o nome do {c}° aluno ? ').strip().title()
  nota = int(input(f'Qual a nota de {nome} ? '))
  if nota > 5:
    situacao = 'Aprovado'
  else:
    situacao = 'Reprovado'
  
  aluno = {
    'Nome do Aluno':nome,
    'Nota do Aluno': nota,
    'Situação': situacao
  }
  
  alunos.append(aluno)

sumario_df = pd.DataFrame(alunos)
display(sumario_df)