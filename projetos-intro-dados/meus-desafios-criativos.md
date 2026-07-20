# 🎯 Resolução do Desafio Criativo: Insights de Feedback (Pix)

Este arquivo contém a resolução passo a passo do desafio de engenharia de prompts aplicado ao contexto de feedbacks sobre os canais digitais de atendimento bancários.

---

## 🧱 Passo 1: Intenção da Análise

Inicialmente, é necessário garantir que todos os feedbacks estão em formato anônimo. Quero que a IA analise os feedbacks sobre uma nova versão de um aplicativo, com novas funcionalidades de acessibilidade, de um banco para identificar reclamações frequentes, elogios, dificuldades de utilização e oportunidades de melhoria. 

O resultado será usado por uma equipe de experiência do cliente, especialista em acessibilidade, para apoiar campanhas de treinamentos, melhorias no aplicativo e nos canais de atendimento de acessibilidade.

A entrega deve conter um resumo detalhado, uma tabela com os temas, exemplos de comentários e recomendações práticas.

O resultado será considerado bom se for claro, organizado, baseado nos comentários fornecidos e útil com foco nas ações a serem tomadas, sejam elas de curto, médio e longo prazo.

---

## 🧱 Passo 2: Contexto e Restrições

- **Contexto:** Estou trabalhando com feedbacks de clientes bancários focados na nova atualização do aplicativo, que introduziu recursos de acessibilidade como leitores de tela aprimorados, navegação por gestos simplificada, ajuste de contraste, tamanho de fonte dinâmico e atendimento em Libras por videochamada.

- **Dados disponíveis:** A base contém a data do feedback, o canal de origem (com usuário anônimo), o texto do comentário, o recurso de acessibilidade citado e o tipo de deficiência, se for informada voluntariamente pelo usuário.

- **Critérios de análise:** A IA deve classificar os feedbacks por tipo de recurso, sentimento (gratidão/elogio, ou frustração por barreira digital e dificuldade de uso) e urgência do ajuste.

- **Cuidados e restrições:**  Como o foco é acessibilidade e anonimato, certifique-se de ignorar qualquer dado pessoal (como nomes ou números de conta). Não invente barreiras técnicas que não estejam explícitas. Se um comentário for ambíguo sobre qual recurso falhou, classifique como "Não Identificado". Use linguagem corporativa, inclusiva, empática e técnica de acessibilidade digital. E selecione uma amostra aleatória dos dados, para avaliação da equipe humanada se todos os critérios estão sendo cumpridos. 

---

## 🚀 Prompt Final Estruturado

Este é o comando pronto para ser utilizado em modelos de LLMs de IA, como Gemini, ChatGPT, Claude, etc.):

```text
Atue como Especialista em acessibilidade digital e analista de experiência do cliente. Sua tarefa é analisar feedbacks sobre a nova versão do aplicativo bancário focado em recursos de acessibilidade para identificar reclamações frequentes, elogios, dificuldades de utilização e oportunidades de melhoria.

Contexto: Inicialmente, garanta que todos os feedbacks sejam tratados em formato anônimo. O resultado desta análise será usado por uma equipe de especialistas em acessibilidade para apoiar campanhas de treinamentos internos, melhorias diretas no aplicativo e evolução nos canais de atendimento inclusivos.

Dados disponíveis:  Serão fornecidos comentários de clientes contendo a data, o canal de origem, o texto descritivo do feedback e o recurso de acessibilidade mencionado.

Instruções de análise:

1. Classifique os feedbacks pelo tipo de acessibilidade afetada.

2. Identifique os principais padrões de elogios, dificuldades de uso e barreiras digitais.Extraia evidências textuais curtas e diretas dos dados fornecidos para ilustrar cada ponto.

3. Sugira recomendações práticas divididas estritamente em ações de curto prazo, médio prazo e longo prazo.

Formato da resposta:

- Resumo Detalhado: Uma análise textual aprofundada sobre o panorama atual do aplicativo em relação à acessibilidade.

- Tabela de Temas: Organizada com as colunas [Tema/Tipo de Acessibilidade | Principal Dificuldade/Elogio | Impacto na Experiência | Exemplo de Comentário Anonimizado].

- Plano de Ação Cronológico: Lista estruturada com as recomendações práticas divididas em blocos de Curto, Médio e Longo Prazo.

Restrições:

Prioridade absoluta para o anonimato: remova ou mascare nomes, números, marcas de celulares ou dados sensíveis. Baseie-se estritamente nos dados fornecidos, sem presumir bugs que não foram relatados. Use uma linguagem clara, organizada, inclusiva e focada em ações concretas.
Ou seja:
- Use apenas os dados fornecidos.
- Não invente números, causas ou conclusões.
- Use linguagem direta, focada em resolver o problema técnico.
```
