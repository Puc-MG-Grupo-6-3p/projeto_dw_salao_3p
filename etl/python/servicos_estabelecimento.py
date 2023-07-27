from base_db_entity import BaseDBEntity
from base_model_csv import BaseModelCsv


class D_Servico(BaseDBEntity):
    def __init__(self, id_servico: int,
                 nome: str = None,
                 valor: float = None,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        super(D_Servico, self).__init__(
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
        self.id_servico = id_servico
        self.nome = nome
        self.valor = valor

    def persiste(self):
        pass

    @classmethod
    def get_by_id(cls, db_conn, db_cursor):
        pass


class ServicosEstabelecimento(BaseModelCsv):
    def __init__(self, id_csv: int = 0,
                 nome: str = None,
                 descricao: str = None,
                 duracao: str = None,
                 categoria: str = None,
                 categoria_padrao: str = None,
                 tipo_preco: str = None,
                 preco_padrao: str = None,
                 preco_promocional: str = None,
                 custo_medio_produtos: str = None,
                 custo_medio_produtos_profissional: str = None,
                 descartaveis_e_outras_despesas: str = None,
                 custo_operacional_estabelecimento: str = None,
                 custo_operacional_profissional: str = None,
                 id_banco: int = None,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        super(ServicosEstabelecimento, self).__init__(
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
        self.descricao = descricao
        self.duracao = duracao
        self.categoria = categoria
        self.categoria_padrao = categoria_padrao
        self.tipo_preco = tipo_preco
        self.preco_padrao = preco_padrao
        self.preco_promocional = preco_promocional
        self.custo_medio_produtos = custo_medio_produtos
        self.custo_medio_produtos_profissional = custo_medio_produtos_profissional
        self.descartaveis_e_outras_despesas = descartaveis_e_outras_despesas
        self.custo_operacional_estabelecimento = custo_operacional_estabelecimento
        self.custo_operacional_profissional = custo_operacional_profissional

        self.servico_dw = None

    def trata_dados(self):
        if not self._is_valid_str(self.categoria):
            self.categoria = None

        if not self._is_valid_str(self.categoria_padrao):
            self.categoria_padrao = None

        self.preco_padrao = self._processa_inteiro(self.preco_padrao)
        self.preco_promocional = self._processa_inteiro(self.preco_promocional)
        self.custo_medio_produtos = self._processa_inteiro(self.custo_medio_produtos)
        self.custo_medio_produtos_profissional = self._processa_inteiro(self.custo_medio_produtos_profissional)
        self.custo_operacional_estabelecimento = self._processa_inteiro(self.custo_operacional_estabelecimento)
        self.custo_operacional_profissional = self._processa_inteiro(self.custo_operacional_profissional)

    def gera_registro_dw(self):
        self.servico_dw = D_Servico(
            nome=self.nome,
            valor=self.preco_padrao)
        self.servico_dw.persiste()
        self.id_banco = self.servico_dw.id_servico

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
            nome=colunas[0],
            descricao=colunas[1],
            duracao=colunas[2],
            categoria=colunas[3],
            categoria_padrao=colunas[4],
            tipo_preco=colunas[5],
            preco_padrao=colunas[6],
            preco_promocional=colunas[7],
            custo_medio_produtos=colunas[8],
            custo_medio_produtos_profissional=colunas[9],
            descartaveis_e_outras_despesas=colunas[10],
            custo_operacional_estabelecimento=colunas[11],
            custo_operacional_profissional=colunas[12],
            id_csv=contador_linha,
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
