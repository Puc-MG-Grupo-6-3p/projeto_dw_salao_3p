create database dw_salao_de_beleza;

use dw_salao_de_beleza;

create table D_Cliente (
  id_cliente integer unsigned primary key not null auto_increment,
  nome varchar(120) not null,
  telefone varchar(20) default null,
  data_nascimento DATE default null,
  email varchar(64) default null
);

create table D_Funcionario (
  id_funcionario integer unsigned primary key not null auto_increment,
  nome varchar(120) not null,
  cargo varchar(64) default null,
  telefone varchar(20) default null
);

create table D_Servico (
  id_servico integer unsigned primary key not null auto_increment,
  nome varchar(120) default null,
  valor float default 0.00
);

CREATE TABLE D_Tempo (
	id_tempo INT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    data DATE NOT NULL,
    hora TIME NOT NULL,
    dia_semana VARCHAR(20) NOT NULL,
    mes VARCHAR(20) NOT NULL,
    trimestre INT NOT NULL,
    semestre INT NOT NULL,
    ano INT NOT NULL
);

create table Fato_Pagamento (
	id_cliente integer unsigned not null,
    id_funcionario integer unsigned not null,
    id_servico integer unsigned not null,
    id_tempo integer unsigned not null,
    valor_total float default 0.00,
    forma_pagamento varchar(255) default null,
    valor_desconto float default 0.00,
    valor_pago float default 0.00,
    primary key(id_cliente, id_funcionario, id_servico, id_tempo),
    key `FK_FatoPagamento_Cliente_idx` (id_cliente),
    key `FK_FatoPagamento_Funcionario` (id_funcionario),
    key `FK_FatoPagamento_Servico` (id_servico),
    key `FK_FatoPagamento_Tempo` (id_tempo),
    constraint `FK_FatoPagamento_Cliente` foreign key (id_cliente) references D_Cliente(id_cliente),
    constraint `FK_FatoPagamento_Funcionario` foreign key (id_funcionario) references D_Funcionario(id_funcionario),
    constraint `FK_FatoPagamento_Servico` foreign key (id_servico) references D_Servico(id_servico),
    constraint `FK_FatoPagamento_Tempo` foreign key (id_tempo) references D_Tempo(id_tempo)
);