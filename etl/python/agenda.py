from base_model_csv import BaseModelCsv
from datetime import datetime


class Agenda(BaseModelCsv):
    def __init__(self, id_csv: int = 0,
                 data: str = None,
                 id_banco: int = None,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        super(Agenda, self).__init__(
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

    def trata_dados(self):
        if self._is_valid_str(self.data):
            self.data = self.processa_data(self.data)
        else:
            self.data = None

    @classmethod
    def processa_linha_csv(cls, linha_csv: str, contador_linha: int,
                           db_conn=None, db_cursor=None,
                           db_host: str = None, db_port: str = None,
                           db_user: str = None, db_password: str = None,
                           db_database: str = None):
        if linha_csv is None or len(linha_csv) == 0:
            return None

        colunas = linha.split(',')
        return cls(
            id_csv=contador_linha,
            data=colunas[0],
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
