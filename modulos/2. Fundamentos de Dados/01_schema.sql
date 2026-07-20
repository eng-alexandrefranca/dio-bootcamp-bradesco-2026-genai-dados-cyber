sql-- Cria o banco de dados se ele não existir

/*
EXPLICAÇÃO TÉCNICA DO SCRIPT:
1. CREATE DATABASE IF NOT EXISTS: Cria o espaço isolado no servidor apenas se ele não existir.
2. USE: Define este banco de dados como o alvo padrão dos comandos seguintes.
3. TIMESTAMP DEFAULT CURRENT_TIMESTAMP: Grava data e hora automaticamente no cadastro.
    TIMESTAMP: É o tipo de dado primitivo. Ele instrui o banco de dados a armazenar valores numéricos que representam data e hora combinadas (no formato AAAA-MM-DD HH:MM:SS), convertendo internamente para o fuso horário UTC.
    DEFAULT CURRENT_TIMESTAMP: É uma restrição de valor padrão. Define que, se uma instrução INSERT criar um novo registro e não fornecer nenhum valor explicitamente para a coluna data_cadastro, o próprio motor do banco de dados capturará o horário exato do relógio do sistema naquele milissegundo e preencherá o campo automaticamente.
*/


CREATE DATABASE IF NOT EXIST db_meu_projeto;

-- Conecta ao banco de dados
USE db_meu_projeto;

-- Cria a tabela de usuários
CREATE TABLE tbl_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);