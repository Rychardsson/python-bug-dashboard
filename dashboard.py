
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('bugs.json')

df_bugs = df[df['tipo'] == 'bug'].copy()

print("--- Relatório: Quantidade de Bugs por Status ---")
status_counts = df_bugs['status'].value_counts()
print(status_counts)
print("\n" + "-"*40 + "\n")

print("--- Relatório: Percentual de Bugs com Prioridade Alta ---")
total_bugs = len(df_bugs)
alta_prioridade_count = len(df_bugs[df_bugs['prioridade'] == 'alta'])
percentual_alta = (alta_prioridade_count / total_bugs) * 100 if total_bugs > 0 else 0
print(f"Total de bugs: {total_bugs}")
print(f"Bugs com prioridade alta: {alta_prioridade_count}")
print(f"Percentual de alta prioridade: {percentual_alta:.2f}%")
print("\n" + "-"*40 + "\n")

print("--- Relatório: Tempo Médio de Resolução de Bugs ---")
df_bugs['data_abertura'] = pd.to_datetime(df_bugs['data_abertura'])
df_bugs['data_fechamento'] = pd.to_datetime(df_bugs['data_fechamento'])

df_fechados = df_bugs[df_bugs['status'] == 'fechado'].copy()
df_fechados['tempo_resolucao'] = df_fechados['data_fechamento'] - df_fechados['data_abertura']
tempo_medio = df_fechados['tempo_resolucao'].mean()
print(f"Tempo médio de resolução: {tempo_medio}")
print("\n" + "-"*40 + "\n")

plt.figure(figsize=(10, 6)) 
status_counts.plot(kind='bar', color='skyblue')
plt.title('Quantidade de Bugs por Status')
plt.xlabel('Status')
plt.ylabel('Quantidade')
plt.xticks(rotation=0) # Deixa os nomes no eixo X na horizontal
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('bugs_por_status.png') 
print("Gráfico 'bugs_por_status.png' gerado com sucesso!")

prioridade_counts = df_bugs['prioridade'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(prioridade_counts, labels=prioridade_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Prioridades dos Bugs')
plt.ylabel('')
plt.savefig('distribuicao_prioridades.png') 
print("Gráfico 'distribuicao_prioridades.png' gerado com sucesso!")