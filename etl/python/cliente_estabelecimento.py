from base_db_entity import BaseDBEntity
from base_model_csv import BaseModelCsv
from datetime import date, datetime


class D_Cliente(BaseDBEntity):
    def __init__(self, nome: str,
                 id_cliente: str = None,
                 telefone: str = None,
                 data_nascimento: date = None,
                 email: str = None,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        super(D_Cliente, self).__init__(
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.email = email

    def persiste(self):
        pass


class Cliente(BaseModelCsv):
    def __init__(self, id_csv: int = 0,
                 cpf: str = None,
                 origem: str = None,
                 nome: str = None,
                 sexo: str = None,
                 telefone_1: str = None,
                 telefone_2: str = None,
                 email: str = None,
                 data_nascimento: str = None,
                 data_cadastro: str = None,
                 observacoes: str = None,
                 pode_agendar_online: str = None,
                 primeiro_agendamento: str = None,
                 status_primeiro_agendamento: str = None,
                 ultimo_agendamento: str = None,
                 status_ultimo_agendamento: str = None,
                 recebe_emails_agendamento: str = None,
                 recebe_emails_programa_fidelidade: str = None,
                 endereco: str = None,
                 numero: str = None,
                 complemento: str = None,
                 bairro: str = None,
                 cidade: str = None,
                 estado: str = None,
                 cep: str = None,
                 como_conheceu_o_salao: str = None,
                 instagram: str = None,
                 id_banco: int = None,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        super(Cliente, self).__init__(
            id_csv=id_csv,
            id_banco=id_banco,
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
        self.cpf = cpf
        self.origem = origem
        self.nome = nome
        self.sexo = sexo
        self.telefone_1 = telefone_1
        self.telefone_2 = telefone_2
        self.email = email
        self.data_nascimento = data_nascimento
        self.data_cadastro = data_cadastro
        self.observacoes = observacoes
        self.pode_agendar_online = pode_agendar_online
        self.primeiro_agendamento = primeiro_agendamento
        self.status_primeiro_agendamento = status_primeiro_agendamento
        self.ultimo_agendamento = ultimo_agendamento
        self.status_ultimo_agendamento = status_ultimo_agendamento
        self.recebe_emails_agendamento = recebe_emails_agendamento
        self.recebe_emails_programa_fidelidade = recebe_emails_programa_fidelidade
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.como_conheceu_o_salao = como_conheceu_o_salao
        self.instagram = instagram
        self.telefone_valido = None

        self.cliente_dw = None

    def trata_dados(self):
        if self.cpf is None or len(self.cpf) == 0 or self.cpf == 'Null':
            self.cpf = None

        if not self._is_valid_str(self.telefone_1):
            self.telefone_1 = None
        if not self._is_valid_str(self.telefone_2):
            self.telefone_2 = None

        if self.telefone_1 is not None:
            self.telefone_valido = self.telefone_1
        elif self.telefone_2 is not None:
            self.telefone_valido = self.telefone_2
        else:
            self.telefone_valido = None

        if not self._is_valid_str(self.email):
            self.email = None

        if self._is_valid_str(self.data_nascimento):
            self.data_nascimento = self._processa_data(self.data_nascimento)

        if self._is_valid_str(self.data_cadastro):
            self.data_cadastro = self._processa_data(self.data_cadastro)

        if not self._is_valid_str(self.observacoes):
            self.observacoes = None

        self.pode_agendar_online = self._processa_sim_nao(self.pode_agendar_online)

        if self._is_valid_str(self.primeiro_agendamento):
            self.primeiro_agendamento = self._processa_data(self.primeiro_agendamento)
        else:
            self.primeiro_agendamento = None

        if self._is_valid_str(self.ultimo_agendamento):
            self.ultimo_agendamento = self._processa_data(self.ultimo_agendamento)
        else:
            self.ultimo_agendamento = None

        if not self._is_valid_str(self.status_primeiro_agendamento):
            self.status_primeiro_agendamento = None
        if not self._is_valid_str(self.status_ultimo_agendamento):
            self.status_ultimo_agendamento = None

        self.recebe_emails_agendamento = \
            self._processa_sim_nao(self.recebe_emails_agendamento)
        self.recebe_emails_programa_fidelidade = \
            self._processa_sim_nao(self.recebe_emails_programa_fidelidade)

        self.cep = None if not self._is_valid_str(self.cep) else self.cep
        self.endereco = None if not self._is_valid_str(self.endereco) else self.endereco
        self.numero = None if not self._is_valid_str(self.numero) else self.numero
        self.complemento = None if not self._is_valid_str(self.complemento) else self.complemento
        self.bairro = None if not self._is_valid_str(self.bairro) else self.bairro
        self.cidade = None if not self._is_valid_str(self.cidade) else self.cidade
        self.estado = None if not self._is_valid_str(self.estado) else self.estado

        if not self._is_valid_str(self.instagram):
            self.instagram = None

        if not self._is_valid_str(self.como_conheceu_o_salao):
            self.como_conheceu_o_salao = None

    def gera_registro_dw(self):
        self.cliente_dw = D_Cliente(
            nome=self.nome,
            telefone=self.telefone_valido,
            data_nascimento=self.data_nascimento
            email=self.email)
        self.cliente_dw.persiste()
        self.id_banco = self.cliente_dw.id_cliente

    @classmethod
    def processa_linha_csv(cls, linha_csv: str, contador_linha: int,
                           db_conn=None, db_cursor=None,
                           db_host: str = None, db_port: str = None,
                           db_user: str = None, db_password: str = None,
                           db_database: str = None):
        if linha_csv is None or len(linha_csv) == 0:
            return None

        colunas = linha_csv.split(',')
        return cls(
            cpf=colunas[0],
            origem=colunas[1],
            nome=colunas[2],
            sexo=colunas[3],
            telefone_1=colunas[4],
            telefone_2=colunas[5],
            email=colunas[6],
            data_nascimento=colunas[7],
            data_cadastro=colunas[8],
            observacoes=colunas[9],
            pode_agendar_online=colunas[10],
            primeiro_agendamento=colunas[11],
            status_primeiro_agendamento=colunas[13],
            ultimo_agendamento=colunas[12],
            status_ultimo_agendamento=colunas[14],
            recebe_emails_agendamento=colunas[15],
            recebe_emails_programa_fidelidade=colunas[16],
            endereco=colunas[19],
            numero=colunas[20],
            complemento=colunas[21],
            bairro=colunas[22],
            cidade=colunas[23],
            estado=colunas[18],
            cep=colunas[17],
            como_conheceu_o_salao=colunas[24],
            instagram=colunas[25],
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
