"""
 Básico
 Princípios Básicos
Desafio
O Banco ByteSafe é conhecido por sua eficiência digital, mas recentemente um bug no sistema causou a duplicação de algumas transações em seu extrato online. Como analista de dados do banco, você foi encarregado de criar uma ferramenta que ajude a identificar e remover essas inconsistências. Cada linha do extrato é uma sequência de identificadores de transações, separados por espaço, e pode conter transações repetidas. Sua missão é garantir que cada transação apareça apenas uma vez, mantendo a ordem da primeira ocorrência. Assim, o extrato ficará limpo e sem duplicatas, facilitando a conferência dos clientes e a auditoria do banco.

Implemente uma função que receba uma string com identificadores de transações separados por espaço e retorne uma nova string, também separada por espaço, contendo apenas a primeira ocorrência de cada transação, na ordem em que aparecem originalmente. Não utilize bibliotecas externas para manipulação de listas ou conjuntos.

Entrada
Uma única linha contendo identificadores de transações separados por espaço. Cada identificador é uma sequência de caracteres alfanuméricos sem espaços.

Saída
Uma única linha contendo os identificadores de transações, separados por espaço, sem repetições e na ordem da primeira ocorrência.

Exemplos
A tabela abaixo apresenta exemplos de entrada e saída:

Entrada	Saída
TX1001 TX1002 TX1001 TX1003	TX1001 TX1002 TX1003
AB12 CD34 AB12 EF56 CD34	AB12 CD34 EF56
QW1 ER2 TY3	QW1 ER2 TY3
AA BB AA AA BB CC	AA BB CC


"""


# Leitura da linha de identificadores de transações
entrada = input()

# Transforma a string de entrada em uma lista de transações individuais
todos_lancamentos = entrada.split()

# Lista para armazenar as transações sem duplicatas
transacoes_unicas = []

# Percorre cada transação e adicione à lista apenas se ainda não estiver presente
for transacao in todos_lancamentos:
    if transacao not in transacoes_unicas:
        transacoes_unicas.append(transacao)

# Imprime o resultado final unindo os elementos com espaço
print(' '.join(transacoes_unicas))
