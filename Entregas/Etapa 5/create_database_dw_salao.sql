create database dw_salao_de_beleza;

use dw_salao_de_beleza;

create table D_Agenda (
  id_agenda integer unsigned primary key not null auto_increment,
  data_hora datetime not null
);

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

create table Fato_Pagamento (
  id_cliente integer unsigned not null,
  id_agenda integer unsigned not null,
  id_funcionario integer unsigned not null,
  id_servico integer unsigned not null,
  valor_total float default 0.00,
  forma_pagamento varchar(255) default null,
  valor_desconto float default 0.00,
  valor_pago float default 0.00,
  primary key(id_cliente, id_agenda, id_funcionario, id_servico),
  key `FK_FatoPagamento_Cliente_idx` (id_cliente),
  key `FK_FatoPagamento_Agenda` (id_agenda),
  key `FK_FatoPagamento_Funcionario` (id_funcionario),
  key `FK_FatoPagamento_Servico` (id_servico),
  constraint `FK_FatoPagamento_Cliente` foreign key (id_cliente) references D_Cliente(id_cliente),
  constraint `FK_FatoPagamento_Agenda` foreign key (id_agenda) references D_Agenda(id_agenda),
  constraint `FK_FatoPagamento_Funcionario` foreign key (id_funcionario) references D_Funcionario(id_funcionario),
  constraint `FK_FatoPagamento_Servico` foreign key (id_servico) references D_Servico(id_servico)
);

