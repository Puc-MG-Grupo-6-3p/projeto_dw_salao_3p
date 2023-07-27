from base_db_entity import BaseDBEntity
from base_model_csv import BaseModelCsv


class D_Funcionario(BaseDBEntity):
    def __init__(self, nome: str,
                 id_funcionario: int = None,
                 cargo: str = None,
                 telefone: str = None,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        super(D_Funcionario, self).__init__(
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cargo = cargo
        self.telefone = telefone

    def persiste(self):
        pass


class Profissional(BaseModelCsv):
    def __init__(self, id_csv: int = 0,
                 nome: str,
                 apelido: str,
                 email: str,
                 telefones: str = None,
                 cpf: str = None,
                 administrador: str = None,
                 tem_agenda: str = None,
                 data_nascimento: str = None,
                 status: str = None,
                 faz_lancamento_pat: str = None,
                 data_inicio: str = None,
                 forma_relacao_profissional: str = None,
                 funcao: str = None,
                 id_banco: int = None,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        super(Profissional, self).__init__(
            id_csv=id_csv,
            id_banco=id_banco,
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
        self.nome = nome
        self.apelido = apelido
        self.email = email
        self.telefones = telefones
        self.cpf = cpf
        self.administrador = administrador
        self.tem_agenda = tem_agenda
        self.data_nascimento = data_nascimento
        self.status = status
        self.faz_lancamento_pat = faz_lancamento_pat
        self.data_inicio = data_inicio
        self.forma_relacao_profissional = forma_relacao_profissional
        self.funcao = funcao

        self.profissional_dw = None

    def trata_dados(self):
        if self.cpf == 'Null':
            self.cpf = None

        if not self._is_valid_str(self.telefones):
            self.telefones = None

        self.administrador = self._processa_sim_nao(self.administrador)
        self.tem_agenda = self._processa_sim_nao(self.tem_agenda)
        self.data_nascimento = self._processa_data(self.data_nascimento)
        self.faz_lancamento_pat = self._processa_sim_nao(self.faz_lancamento_pat)
        self.data_inicio = self._processa_data(self.data_inicio)

        if self.forma_relacao_profissional is None or len(self.forma_relacao_profissional) == 0:
            self.forma_relacao_profissional = None

        if self.funcao is None or len(self.funcao) == 0:
            self.funcao = None

    def gera_registro_dw(self):
        self.profissional_dw = D_Funcionario(
            nome=self.nome,
            cargo=self.funcao,
            telefone=self.telefones)
        self.profissional_dw.persiste()
        self.id_banco = self.profissional_dw.id_funcionario

    @classmethod
    def processa_linha_csv(cls, linha_csv: str, contador_linha: int,
                           db_conn=None, db_cursor=None,
                           db_host: str = None, db_port: str = None,
                           db_database: str = None,
                           db_user: str = None, db_password: str = None):
        if linha_csv is None or len(linha_csv) == 0:
            return None

        colunas = linha_csv.split(',')
        return cls(
            id_csv=contador_linha,
            nome=colunas[0],
            apelido=colunas[1],
            email=colunas[2],
            cpf=colunas[3],
            administrador=colunas[4],
            tem_agenda=colunas[5],
            data_nascimento=colunas[6],
            status=colunas[7],
            faz_lancamento_pat=colunas[8],
            data_inicio=colunas[9],
            forma_relacao_profissional=colunas[10],
            funcao=colunas[11],
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)