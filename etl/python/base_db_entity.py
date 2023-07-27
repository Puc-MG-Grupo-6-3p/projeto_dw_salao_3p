class BaseDBEntity:
	def __init__(self, nome_tabela: str,
				 db_conn=None,
				 db_cursor=None,
				 db_host: str = None,
				 db_port: str = None,
				 db_user: str = None,
				 db_password: str = None,
				 db_database: str = None):
		self.nome_tabela = nome_tabela
		self.db_conn = db_conn
		self.db_cursor = db_cursor
		self.db_user = db_user
		self.db_password = db_password
		self.db_database = db_database

	@classmethod
	def get_connection(cls, db_conn, db_cursor):
		if db_conn is None or not db_conn.is_connected():
			raise Exception('Não há conexão com o banco de dados')

		if db_cursor is None:
			db_cursor = db_conn.cursor()

		return db_conn, db_cursor
