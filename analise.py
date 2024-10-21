import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('seguro_de_vida.csv',sep=',')
print(dados.head(5))

print(dados[['idade','imc', 'despesas']].describe())

#Percentual de fumantes
cat_fumantes = dados['fumante'].value_counts()
total_observacoes = dados.shape[0]
percentual_fumantes = (cat_fumantes['sim'] / total_observacoes) * 100
print("O percentual de fumantes na base de dados é:", percentual_fumantes, "%")
#20,4%


dados[['despesas']].hist(figsize=(8,8))


plt.figure(figsize=(8,5))
sns.histplot(dados['idade'], bins=20, kde=True, color='red')  
plt.title('Distribuição de idade dos Clientes')
plt.xlabel('idade')
plt.ylabel('Frequência')
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='fumante', y='imc', data=dados, hue='fumante', palette='coolwarm', dodge=False)
plt.title('IMC por Status de Fumante')
plt.xlabel('Fumante')
plt.ylabel('IMC')
plt.legend([],[], frameon=False) 
plt.show()



plt.figure(figsize=(8,5))
sns.scatterplot(x='idade', y='despesas', data=dados, hue='fumante', palette='coolwarm')
plt.title('Idade vs. Despesas Médicas')
plt.xlabel('Idade')
plt.ylabel('Despesas Médicas')
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(dados['despesas'], bins=30, kde=True, color='green')
plt.title('Distribuição das Despesas Médicas')
plt.xlabel('Despesas')
plt.ylabel('Frequência')
plt.show()

plt.figure(figsize=(8,5))
sns.violinplot(x='fumante', y='despesas', data=dados, hue='fumante', palette='coolwarm', legend=False)
plt.title('Comparação de Despesas Médicas entre Fumantes e Não Fumantes')
plt.xlabel('Fumante')
plt.ylabel('Despesas Médicas')
plt.show()



# Matriz
dados = dados.astype({'idade': 'float64', 'imc': 'float64', 'despesas': 'float64'})
matriz_correlacao = dados[['idade','imc','filhos','despesas']].corr()
plt.figure(figsize=(10, 8)) 
sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlação')
plt.show()