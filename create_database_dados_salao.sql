CREATE DATABASE  IF NOT EXISTS salao_de_beleza;
USE salao_de_beleza;

-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
-- Host: localhost    Database: salao_de_beleza
-- ------------------------------------------------------
-- Server version	8.0.31

DROP TABLE IF EXISTS clientes;
CREATE TABLE clientes (
	nome text,
	telefone text,
	data_nascimento date DEFAULT NULL,
	email text,
	seq_id int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (seq_id)
);


DROP TABLE IF EXISTS funcionario;
CREATE TABLE funcionario (
	nome text,
	cargo text,
	telefone text,
	seq_id int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (seq_id)
);


DROP TABLE IF EXISTS pagamento;
CREATE TABLE pagamento (
	valor_total int DEFAULT NULL,
	valor_desconto int DEFAULT NULL,
	valor_pago int DEFAULT NULL,
	forma_de_pagamento text,
	id_cliente int DEFAULT NULL,
	seq_id int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (seq_id),
	KEY FK_PAGAMENTO_CLIENTE_idx (id_cliente),
	CONSTRAINT FK_PAGAMENTO_CLIENTE FOREIGN KEY (id_cliente) REFERENCES clientes(seq_id)
);


DROP TABLE IF EXISTS servico;
CREATE TABLE servico (
	nome_servico text,
	valor_servico int DEFAULT NULL,
	seq_id int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY(seq_id)
);


DROP TABLE IF EXISTS agenda;
CREATE TABLE agenda (
	data_hora datetime DEFAULT NULL,
	id_cliente int DEFAULT NULL,
	id_funcionario int DEFAULT NULL,
	id_servico int DEFAULT NULL,
	seq_id int NOT NULL AUTO_INCREMENT,
	id_pagamento int DEFAULT NULL,
	PRIMARY KEY (seq_id),
	KEY FK_AGENDA_CLIENTE_idx (id_cliente),
	KEY FK_AGENDA_FUNCIONARIO_idx (id_funcionario),
	KEY FK_AGENDA_SERVICO_idx (id_servico),
	KEY FK_AGENDA_PAGAMENTO_idx (id_pagamento),
	CONSTRAINT FK_AGENDA_CLIENTE FOREIGN KEY (id_cliente) REFERENCES clientes (seq_id),
	CONSTRAINT FK_AGENDA_FUNCIONARIO FOREIGN KEY (id_funcionario) REFERENCES funcionario (seq_id),
	CONSTRAINT FK_AGENDA_PAGAMENTO FOREIGN KEY (id_pagamento) REFERENCES pagamento (seq_id),
	CONSTRAINT FK_AGENDA_SERVICO FOREIGN KEY (id_servico) REFERENCES servico (seq_id)
);


LOCK TABLES funcionario WRITE;
INSERT INTO funcionario
VALUES ('Telmara', 'Manicure', NULL, 1),
	   ('Janaina', 'Auxiliar de Cabelereira', NULL, 2),
	   ('Vanessa', 'Auxiliar de Cabelereira', NULL, 3),
	   ('Nelly', 'Cabelereira', NULL, 4),
	   ('Cristiane ', 'Dona e Cabelereira', NULL, 5),
	   ('Maiane', 'Cabelereira', NULL, 6);
UNLOCK TABLES;