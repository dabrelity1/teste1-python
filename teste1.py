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

media_notas_sexo = df.groupby('Sexo').mean()
media_notas_sexo.plot(kind='bar')
