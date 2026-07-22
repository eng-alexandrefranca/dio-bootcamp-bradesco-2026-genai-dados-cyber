# 💳 Detecção de Anomalias em Cartão de Crédito

Este repositório foi criado para fins educacionais com o objetivo de estudar técnicas de **Detecção de Anomalias** e **Ciência de Dados** utilizando transações de cartão de crédito.

O foco principal é resolver o problema do extremo desbalanceamento de dados utilizando a técnica **SMOTE** (Synthetic Minority Over-sampling Technique) combinada com o algoritmo **Random Forest**.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas & NumPy** (Manipulação de dados)
* **Scikit-Learn** (Algoritmos de Machine Learning)
* **Imbalanced-Learn (SMOTE)** (Balanceamento de dados artificiais)
* **Matplotlib & Seaborn** (Visualização de dados/Gráficos)

---

## 📁 Estrutura do Projeto

* `data/`: Pasta destinada a armazenar o arquivo `.csv` baixado (opcional, já que o script pode baixar direto).
* `notebooks/`: Contém os arquivos de códigos estruturados passo a passo.
* `requirements.txt`: Arquivo com a lista de todas as bibliotecas necessárias instaladas.

---

## 🚀 Como Rodar Este Projeto Localmente

### 1. Clonar o repositório
Abra o seu terminal ou prompt de comando e execute:
```bash
git clone https://github.com
cd NOME-DO-REPOSITORIO
```

### 2. Instalar as Dependências
Instale todas as bibliotecas necessárias rodando os comandos:
```bash
pip install -r requirements.txt
```

```bash
python -m pip install --upgrade pip
```

### 3. Executar o Script
Navegue até a pasta de notebooks ou scripts e execute o arquivo Python principal:
```bash
python notebooks/detector_anomalias.py
```

---

## 📊 Metodologia Aplicada

1. **Carga e Limpeza**: Importação de dados reais de cartões anonimizados.
2. **Normalização**: Escalonamento de variáveis de tempo e valor (`StandardScaler`).
3. **Over-sampling (SMOTE)**: Geração de fraudes sintéticas para equilibrar o treino do modelo.
4. **Treinamento e Avaliação**: Uso do `Random Forest Classifier` avaliado por matriz de confusão e métricas de precisão.
