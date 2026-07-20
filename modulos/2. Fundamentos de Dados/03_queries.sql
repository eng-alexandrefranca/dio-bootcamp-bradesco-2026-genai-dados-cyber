-- Consultas

USE  db_meu_projeto;

-- Buscar todos os usuários cadastrados
SELECT * FROM tbl_usuarios;

-- Buscar apenas um usuário pelo e-mail
SELECT * FROM tbl_usuarios WHERE email = 'ana.silva@email.com';

-- Atualizar o nome de um usuário específico
UPDATE tbl_usuarios SET nome = 'Ana Silva Souza' WHERE id = 1;
