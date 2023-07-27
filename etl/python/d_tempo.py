from base_db_entity import BaseDBEntity
from datetime import date, datetime, time


class D_Tempo(BaseDBEntity):
    def __init__(self, id_tempo: int,
                 data: date,
                 hora: time,
                 dia_semana: str,
                 mes: str,
                 trimestre: int,
                 semestre: int,
                 ano: int,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        super(D_Tempo, self).__init__(
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
        self.id_tempo = id_tempo
        self.data = data
        self.hora = hora
        self.dia_semana = dia_semana
        self.mes = mes
        self.trimestre = trimestre
        self.semestre = semestre
        self.ano = ano

    def persiste(self):
        pass
