from base_model_csv import BaseModelCsv


class Agendamento(BaseModelCsv):
    def __init__(self, id_csv: int = 0,
                 data: str,
                 hora: str,
                 profissional: str,
                 assistente: str = None,
                 categoria_servico: str = None,
                 servico: str = None,
                 duracao: str = None,
                 cliente: str = None,
                 sexo: str = None,
                 telefones: str,
                 email: str = None,
                 valor: str = None,
                 fechamento_conta: str = None,
                 status: str = None,
                 cadastramento: str = None,
                 data_cadastro_cliente: str = None,
                 responsavel_agendamento: str = None,
                 origem: str = None,
                 observacoes: str = None,
                 id_banco: int = None,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        super(Agendamento, self).__init__(
            id_csv=id_csv,
            id_banco=id_banco,
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
        self.data = data
        self.hora = hora
        self.profissional = profissional
        self.assistente = assistente
        self.categoria_servico = categoria_servico
        self.servico = servico
        self.duracao = duracao
        self.cliente = cliente
        self.sexo = sexo
        self.telefone = telefone
        self.email = email
        self.valor = valor
        self.fechamento_conta = fechamento_conta
        self.status = status
        self.cadastramento = cadastramento
        self.data_cadastro_cliente = data_cadastro_cliente
        self.responsavel_agendamento = responsavel_agendamento
        self.origem = origem
        self.observacoes = observacoes

        self.data_hora = None

    def trata_dados(self):
        self.data = datetime.strptime(self.data, '%Y-%m-%d').date()

        if self.hora is not None and len(self.hora) > 0:
            hr_partes = self.hora.split(':')
            self.data_hora = datetime(
                year=self.data.year,
                month=self.data.month,
                day=self.data.day,
                hour=int(hr_partes[0]),
                minute=int(hr_partes[1]),
                second=0)
        else:
            self.data_hora = datetime(
                year=self.data.year,
                month=self.data.month,
                day=self.data.day,
                hour=0,
                minute=0,
                second=0)

        if self.assistente is None or len(self.assistente) == 0:
            self.assistente = None

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
            id_csv=contador_linha,
            data=colunas[0],
            hora=colunas[1],
            profissional=colunas[2],
            assistente=colunas[3],
            categoria_servico=colunas[4],
            servico=colunas[5],
            duracao=colunas[6],
            cliente=colunas[7],
            sexo=colunas[8],
            telefone=colunas[9],
            email=colunas[10],
            valor=colunas[11],
            fechamento_conta=colunas[12],
            status=colunas[13],
            cadastramento=colunas[14],
            data_cadastro_cliente=colunas[15],
            responsavel_agendamento=colunas[16],
            origem=colunas[17],
            observacoes=colunas[18],
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
