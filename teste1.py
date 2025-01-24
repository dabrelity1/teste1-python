import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar o ficheiro Excel
file_path = 'notas_exames_alunos.xlsx'
df = pd.read_excel(file_path)

# 1. Distribuição de frequências por sexo e concelho
print("Distribuição de frequências por sexo e concelho:")
freq_sexo_concelho = df.groupby(['Sexo', 'Concelho']).size().unstack()
print(freq_sexo_concelho)

# 2. Percentagem de alunos por concelho
print("\n")
print("Percentagem de alunos por concelho:")
percent_alunos_concelho = df['Concelho'].value_counts(normalize=True) * 100
print(percent_alunos_concelho)

# 3. Nota média de Matemática para alunos de cada estado civil

print("\n")
nota_media_matematica_tipo_civil = df.groupby('Estado civil')['Matematica'].mean()
print("Nota média de matemática por estado civil:")
print(nota_media_matematica_tipo_civil)

# 4. Idade média dos alunos que tiveram as 5 maiores notas em Estatística

print("\n")
print("Idade média dos alunos que tiveram as 5 maiores notas em Estatística:")
top_5_estatistica = df.nlargest(5, 'Estatistica')
idade_media_top_5_estatistica = top_5_estatistica['Idade'].mean()
print(idade_media_top_5_estatistica)

# 5. Gráfico de colunas para comparar as notas médias por sexo em cada disciplina

disciplinas = ['Matematica', 'Estatistica', 'Portugues', 'Ingles']  # Adicione outras disciplinas conforme necessário
media_notas_sexo = df.groupby('Sexo')[disciplinas].mean()
media_notas_sexo.plot(kind='bar')
plt.show()

# 6. Gráfico circular para visualizar a distribuição percentual de alunos por "Local do exame"
percent_local_exame = df['Local do exame'].value_counts(normalize=True) * 100
percent_local_exame.plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuição Percentual de Alunos por Local do Exame')
plt.ylabel('')
plt.show()

# 7. Número de alunos por estado civil que têm notas inferiores a 10 em Matemática
alunos_notas_baixas = df[df['Matematica'] < 10]
num_alunos_estado_civil_10 = alunos_notas_baixas['Estado civil'].value_counts()
print(num_alunos_estado_civil_10)

# 8. Lista de alunos que tiveram 20 em Estatística
alunos_20_estatistica = df[df['Estatistica'] == 20]
print(alunos_20_estatistica)

# 9. Gráfico de barras para mostrar o número de alunos por concelho
num_alunos_concelho = df['Concelho'].value_counts()
num_alunos_concelho.plot(kind='bar')
plt.title('Número de Alunos por Concelho')
plt.xlabel('Concelho')
plt.ylabel('Número de Alunos')
plt.show()

# 10. Listar os primeiros 10 registos do ficheiro mas somente as colunas, Id Aluno, Matemática e Estatística
primeiros_10_registos = df[['Id aluno', 'Matematica', 'Estatistica']].head(10)
print(primeiros_10_registos)

# 11. Nota média de Estatística para alunos com menos de 20 anos e que sejam solteiros
media_estatistica_jovens_solteiros = df[(df['Idade'] < 20) & (df['Estado civil'] == 'Solteiro')]['Estatistica'].mean()
print(media_estatistica_jovens_solteiros)

# 12. Gráfico de colunas com a média das notas dos alunos sendo ou não trabalhador estudante
media_notas_trabalhador_estudante = df.groupby('Trabalhador estudante').mean()
media_notas_trabalhador_estudante.plot(kind='bar')
plt.title('Média das Notas: Trabalhador estudante vs Não Trabalhador estudante')
plt.xlabel('Trabalhador estudante')
plt.ylabel('Nota Média')
plt.show()