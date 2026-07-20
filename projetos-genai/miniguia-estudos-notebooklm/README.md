# 📘 Miniguia de Estudos com NotebookLM: Introdução às Finanças Pessoais

Este repositório foi desenvolvido como parte de um desafio de projeto na **DIO (Digital Innovation One)**. O objetivo principal é utilizar o Google NotebookLM como uma ferramenta de aprendizagem ativa, aplicando curadoria de fontes, pensamento crítico e engenharia de prompts para criar um caderno temático sobre finanças.

---

## 🎯 1. Contexto e Objetivos

### Contexto

O entendimento sobre **Finanças Pessoais** é fundamental para o desenvolvimento da autonomia financeira. Este caderno temático foi concebido para estruturar conceitos básicos sobre o assunto, utilizando inteligência artificial para otimizar o processo de absorção do conteúdo.

### Objetivos de Estudo

* **Aprender a elaborar e gerir um orçamento pessoal ou familiar**.

* **Desenvolver a habilidade de distinguir necessidades de desejos nas decisões de compra**.

* **Compreender o funcionamento dos juros e a importância da reserva de emergência**.

---

## 📚 2. Curadoria de Fontes

Para alimentar o NotebookLM, foram selecionadas **04** fontes abertas e confiáveis em formato de texto/PDF. Abaixo estão listados os materiais utilizados:

1. **Caderno de Educação Financeira do Banco Central** - https://www.bcb.gov.br/content/cidadaniafinanceira/documentos_cidadania/Cuidando_do_seu_dinheiro_Gestao_de_Financas_Pessoais/caderno_cidadania_financeira.pdf

2. **Revista de Educação Financeira do Conselho Federal de Contabilidade** - Link de Acesso: https://cfc.org.br/wp-content/uploads/2025/07/RBC271_jan_fev.pdf

3. **Educação Financeira do Bradesco Seguros** - https://www.bradescoseguros.com.br/wcm/connect/04ac6b17-6651-467e-a4b4-9a080f42e009/05_ETAPAS_02.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-04ac6b17-6651-467e-a4b4-9a080f42e009-phFrp6U

4. **Finanças Pessoais para Iniciantes da Universidade Federal de Alagoas** - https://www.repositorio.ufal.br/bitstream/riufal/7121/1/Finan%C3%A7as%20pessoais%20para%20iniciantes.pdf

---

## 🧠 3. Engenharia de Prompts e "Cicatrizes" (Troubleshooting)

Nesta seção está documentado o processo de refinamento das perguntas para extrair o melhor resultado da IA com base estrita nas fontes fornecidas.

### Prompt Inicial (Tentativa e Erro)
> **Prompt:** "Me explica o que é finanças."
* **Resultado:** A resposta ficou com analogias, trechos foram referenciados com as fontes e não utilizou uma lingguagem muito técnica ou acadêmica.

### Prompt Refinado (Versão Final Empregada)
> **Prompt:** "Atue como um professor de finanças. Com base na fonte do Banco Central, explique o conceito de finanças utilizando uma analogia simples do dia a dia. Cite a página ou seção de referência."
* **Resultado:** Resposta precisa, didática e diretamente ancorada no material de estudo.

### Cicatrizes / Aprendizados (Troubleshooting)
* **Desafio:** A IA apresentou respostas tentando misturar os dados das fontes diferentes.
* **Solução:** Adicionei a restrição "Com base exclusivamente na Fonte X" no início de cada comando.

---

## 🚀 4. Miniguia de Estudo (Entrega Final)

### 📋 Resumos Estruturados

* **Fundamentos Essenciais (O que eu preciso saber primeiro):**

  * **Educação vs. Alfabetização Financeira:** Enquanto a alfabetização foca no conhecimento e atitude, a educação financeira é a competência de aplicar esse conhecimento para gerar qualidade de vida e tomar decisões eficientes.

  * **A Regra do 85/15:** O planejamento financeiro é composto por 85% de comportamento e apenas 15% de matemática. O sucesso depende mais de hábitos saudáveis do que de cálculos complexos.

  * **Troca Intertemporal:** É o conceito central das finanças. Consiste na escolha entre consumir agora (usando crédito e pagando juros) ou poupar agora para consumir mais no futuro (recebendo juros)

  * **Necessidade vs. Desejo:** Saber distinguir o que é indispensável para a vida (necessidade) do que é apenas uma vontade ou anseio (desejo) é a base para o equilíbrio das contas. Orçamento Superavitário: O objetivo fundamental é garantir que as receitas sejam sempre maiores que as despesas (Receitas - Despesas = Poupança).
  
  * **O Tripé dos Investimentos:** Todo investimento deve ser avaliado com base em sua liquidez (velocidade de virar dinheiro), risco (chance de perda) e rentabilidade (retorno financeiro)

* **Erros Comuns ou Riscos (O que evitar):**

  * **Consumo por Impulso:** Decisões guiadas pela emoção, pelo imediatismo ou pelo marketing de sedução levam ao desequilíbrio e ao arrependimento.
  * **Uso Inadequado do Crédito:** Ver o crédito como uma extensão da renda, e não como um recurso de terceiros que possui um custo (juros).

  * **Armadilhas de Marketing:** Técnicas como preços terminados em "99 centavos", parcelas que parecem pequenas ("custa apenas um cafezinho por dia") e a criação de falsas sensações de escassez.

  * **Esquecer Despesas Sazonais:** Muitas dívidas surgem por falta de planejamento para gastos anuais previsíveis, como IPTU, IPVA e material escolar.

  * **Crédito "Fácil" e Fraudes:** Ofertas de dinheiro rápido geralmente escondem as maiores taxas de juros (CET elevado) ou golpes financeiros, especialmente no ambiente digital.
  
  * **Poupar apenas o que sobra:** Deixar para guardar dinheiro no fim do mês é pouco efetivo, pois geralmente não sobra nada após gastos não planejados.

* **Próximos Passos Práticos:**  

  * **Pague-se Primeiro:** Assim que receber sua renda, separe imediatamente a parte destinada à poupança/investimento antes de pagar as outras contas

  * **Registre e Agrupe:** Anote diariamente todas as receitas e despesas. Agrupe-as em categorias (essenciais, supérfluos e desperdícios) para identificar onde é possível cortar gastos

  * **Transforme Sonhos em Projetos:** Tire os desejos do imaginário e coloque-os no papel com metas claras, prazos definidos (curto, médio ou longo prazo) e etapas intermediárias para comemorar

  * **Crie uma Reserva de Emergência:** Construa um fundo de segurança de, no mínimo, cinco vezes o valor do seu salário para enfrentar imprevistos sem recorrer a dívidas.

  * **Consuma de Forma Consciente:** Antes de comprar, pergunte-se: "Eu preciso?", "Eu posso?" e "Tem que ser agora?". Sempre use uma lista de compras e evite ir ao mercado com fome.

  * **Avalie o CET:** Ao contratar crédito, não olhe apenas para o valor da parcela, mas para o Custo Efetivo Total (CET), que inclui taxas, impostos e seguros


### 📖 Glossário de Conceitos:
* **Educação Financeira:** É o processo de promover comportamentos que melhorem a cidadania e o bem-estar, capacitando o cidadão a gerenciar seus recursos de forma autônoma e consciente.
* **Orçamento:** Ferramenta de planejamento que permite registrar e organizar receitas e despesas para realizar sonhos e garantir que os gastos não superem os ganhos.
* **Troca Intertemporal:** Conceito central que envolve a decisão entre consumir agora (podendo gerar dívidas e juros) ou poupar no presente para consumir mais ou com segurança no futuro.
* **Necessidade vs. Desejo:** Diferenciação essencial entre o que é indispensável para a vida (necessidade) e as vontades ou anseios que trazem prazer, mas podem ser adiados (desejo).
* **Reserva de Emergência:** Fundo de segurança destinado a cobrir imprevistos (como desemprego ou doenças), idealmente equivalente a, no mínimo, cinco vezes o valor do seu salário.

### 🔄 Prompts Reutilizáveis para Revisão

Você pode copiar e colar estes prompts no seu NotebookLM para revisar esta matéria:

1. `Crie um quiz de 5 perguntas de múltipla escolha sobre os conceitos de finanças, baseando-se apenas nos documentos do Banco Central.`
2. `Gere um resumo em tópicos (bullet points) destacando os 3 riscos mais importantes citados na Fonte 1.`

---

## 🛠️ Tecnologias Utilizadas
* **Google NotebookLM** - Para análise de documentos e geração de insights.
* **GitHub** - Para hospedagem do portfólio e documentação.

---
Desenvolvido por **Alexandre** ✨  
Conecte-se comigo no [LinkedIn](https://www.linkedin.com/)
