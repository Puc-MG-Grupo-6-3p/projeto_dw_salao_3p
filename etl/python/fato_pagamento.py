from base_db_entity import BaseDBEntity


class FatoPagamento:
    def __init__(self, id_cliente: int,
                 id_funcionario: int,
                 id_servico: int,
                 valor_total: float = None,
                 forma_pagamento: str = None,
                 valor_desconto: float = None,
                 valor_pago: float = None,
                 db_conn=None,
                 db_cursor=None,
                 db_host: str = None,
                 db_port: str = None,
                 db_user: str = None,
                 db_password: str = None,
                 db_database: str = None):
        super(FatoPagamento, self).__init__(
            db_conn=db_conn,
            db_cursor=db_cursor,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_database=db_database)
        self.id_client = id_cliente
        self.id_funcionario = id_funcionario
        self.id_servico = id_servico
        self.valor_total = valor_total
        self.forma_pagamento = forma_pagamento
        self.valor_desconto = valor_desconto
        self.valor_pago = valor_pago

    def persiste(self):
        pass
