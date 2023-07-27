class BaseModelCsv:
    def __init__(self, id_csv: int,
                 id_banco: int = None,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        self.id_csv = id_csv
        self.id_banco = id_banco
        self.db_conn = db_conn
        self.db_cursor = db_cursor

        # Dados para renovação da conexão com o banco de dados
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_password = db_password
        self.db_database = db_database

    def _is_valid_str(self, txt):
        if not isinstance(txt, str):
            raise Exception('Por favor forneça uma string')

        if txt is None or len(txt) == 0:
            return False
        return True

    def _processa_data(self, txt):
        dt_partes = txt.split('/')
        dt = datetime(
            year=dt_partes[2],
            month=dt_partes[1],
            day=dt_partes[0],
            hour=0,
            minute=0,
            second=0).date()
        return dt

    def _processa_sim_nao(self, txt):
        if self._is_valid_str(txt):
            if txt in ('Sim', 'Não'):
                if txt == 'Sim':
                    return True
                return False
        return False

    def _processa_inteiro(self, txt):
        if not isinstance(txt, str):
            raise Exception('O parâmetro fornecido deve ser um número')

        if txt is None or len(txt) == 0:
            return None
        return int(txt)

    def trata_dados(self):
        pass

    def gera_registro_dw(self):
        pass
