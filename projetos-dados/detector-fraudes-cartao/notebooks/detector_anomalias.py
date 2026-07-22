import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
# Importando o SMOTE da biblioteca imblearn
from imblearn.over_sampling import SMOTE

#import kagglehub

#echo "creditcard.csv" >> .gitignore

#git lfs migrate import --include="modulos/5. Análise de Dados com Python/5.8. Desafio de Projeto/data/creditcard.csv" --everything


# 1. Carregar os dados https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

"""
url = "https://githubusercontent.com"
df = pd.read_csv(url)
"""

"""
print("Baixando o dataset do Kaggle... Isso pode levar alguns segundos.")
path_diretorio = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
caminho_csv = "data/creditcard.csv"
"""

print("Carregando o dataset localmente da pasta data/...")
caminho_csv = "data/creditcard.csv"

df = pd.read_csv(caminho_csv)
print("Dataset carregado com sucesso! Dimensões:", df.shape)


# 2. Separar em X (dados da transação) e y (se é fraude ou não)
X = df.drop(columns=['Class'])
y = df['Class']

# 3. Separar em dados de Treino e dados de Teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Padronizar as colunas que estão em escalas muito diferentes (tempo e valor)
scaler = StandardScaler()
features_to_scale = ['Time', 'Amount']
X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()

X_train_scaled[features_to_scale] = scaler.fit_transform(X_train[features_to_scale])
X_test_scaled[features_to_scale] = scaler.transform(X_test[features_to_scale])

# -------------------------------------------------------------
# O PULO DO GATO: Aplicar o SMOTE APENAS nos dados de treino!
# Nunca aplicamos no teste, pois o teste deve refletir o mundo real.
# -------------------------------------------------------------
print("Fraudes antes do SMOTE:", y_train.sum())

smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train_scaled, y_train)

print("Fraudes criadas após o SMOTE:", y_train_balanced.sum())
# -------------------------------------------------------------

# 5. Treinar o modelo clássico (Random Forest) com os dados balanceados
modelo = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)
modelo.fit(X_train_balanced, y_train_balanced)

# 6. Testar o modelo com os dados de teste reais
y_pred = modelo.predict(X_test_scaled)

# 7. Exibir os resultados
print("\n--- Matriz de Confusão ---")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\n--- Relatório de Performance ---")
print(classification_report(y_test, y_pred))

# Plotar gráfico bonito para ver os acertos e erros
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=['Normal', 'Fraude'], yticklabels=['Normal', 'Fraude'])
plt.ylabel('Realidade (O que era)')
plt.xlabel('Previsão do Computador')
plt.title('Resultados com SMOTE + Random Forest')
plt.show()
