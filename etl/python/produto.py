from base_model_csv import BaseModelCsv


class Produto(BaseModelCsv):
    def __init__(self, id_csv: int = 0,
                 nome: str,
                 categoria: str,
                 fabricante: str = None,
                 codigo_identificacao: str = None,
                 revenda: str = None,
                 preco: str = None,
                 preco_revenda_profissional: str = None,
                 comissao: str = None,
                 unidade_medida: str = None,
                 medidas_por_unidade: str = None,
                 precos_por_medida: str = None,
                 codigo_barras: str = None,
                 status: str = None,
                 valor_compra: str = None,
                 id_banco: int = None,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        super(Produto, self).__init__(
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
        self.categoria = categoria
        self.fabricante = fabricante
        self.codigo_identificacao = codigo_identificacao
        self.revenda = revenda
        self.preco = preco
        self.preco_revenda_profissional = preco_revenda_profissional
        self.comissao = comissao
        self.unidade_medida = unidade_medida
        self.medidas_por_unidade = medidas_por_unidade
        self.precos_por_medida = precos_por_medida
        self.codigo_barras = codigo_barras
        self.status = status
        self.valor_compra = valor_compra

    def trata_dados(self):
        if '"' in self.nome:
            self.nome = self.nome.replace('"', '')

        if '"' in self.categoria:
            self.categoria = self.categoria.replace('"', '')

        if self.fabricante is None or len(self.fabricante) == 0:
            self.fabricante = None
        else:
            if '"' in self.fabricante:
                self.fabricante = self.fabricante.replace('"', '')

        if '"' in self.codigo_identificacao:
            self.codigo_identificacao = self.codigo_identificacao.replace('"', '')
        if self.codigo_identificacao is None or len(self.codigo_identificacao) == 0:
            self.codigo_identificacao = None

        if self.revenda is None or len(self.revenda) == 0:
            self.revenda = None
        else:
            if '"' in self.revenda:
                self.revenda = self.revenda.replace('"', '')

            if self.revenda not in ('Sim', 'Não'):
                self.revenda = None
            else:
                self.revenda = self.revenda == 'Sim'

        self.preco = self._trata_int(self.preco)
        self.preco_revenda_profissional = self._trata_int(self.preco_revenda_profissional)
        self.comissao = self._trata_int(self.comissao)
        self.unidade_medida = self._trata_int(self.unidade_medida)
        self.medidas_por_unidade = self._trata_int(self.medidas_por_unidade)
        self.preco_por_medida = self._trata_int(self.preco_por_medida)
        self.valor_compra = self._trata_int(self.valor_compra)

        if not self._is_valid_str(self.status):
            self.status = None

    def _trata_int(self, int_str):
        if not isinstance(int_str, str):
            raise Exception('O valor de entrada deve ser um inteiro')

        if '"' in int_str:
            int_str = int_str.replace('"', '')
        if int_str is None or len(int_str) == 0:
            return 0
        else:
            return int(int_str)

    @classmethod
    def processa_linha_csv(cls, linha_csv: str, contador_linha: int,
                           db_conn=None, db_cursor=None,
                           db_host=None, db_port=None, db_database=None,
                           db_user=None, db_password=None):
        if linha_csv is None or len(linha_csv) == 0:
            return None

        colunas = linha_csv.split(',')
        return cls(
            id_csv=contador_linha,
            nome=colunas[0],
            categoria=colunas[1],
            fabricante=colunas[2],
            codigo_identificacao=colunas[3],
            revenda=colunas[4],
            preco=colunas[5],
            preco_revenda_profissional=colunas[6],
            comissao=colunas[7],
            unidade_medida=colunas[8],
            medidas_por_unidade=colunas[9],
            preco_por_medida=colunas[10],
            codigo_barras=colunas[11],
            status=colunas[12],
            valor_compra=colunas[13],
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
