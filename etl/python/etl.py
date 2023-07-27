from agenda import Agenda
from agendamento import Agendamento
from cliente_estabelecimento import Cliente
from fato_pagamento import FatoPagamento
from produto import Produto
from profissionais import D_Funcionario, Profissional
from servicos_estabelecimento import D_Servico, ServicosEstabelecimento
import os


# Configurações para conexão com banco de dados
host = '127.0.0.1'
porta = '3306'
database = 'dw_salao_de_beleza'
user = 'root'
password = 'Al,2101,CD@'


path_arquivos = f'{os.sep}Users{os.sep}anselmo_lira{os.sep}documents{os.sep}faculdades_cursos{os.sep}big_data{os.sep}puc_mg{os.sep}3p{os.sep}Projeto{os.sep}dados_para_dw'


mapa_arquivo_processador = {
    'agenda': {
        'arquivo': 'agenda.csv'
        'processador': Agenda,
        'registros': []
    },
    'agendamento': {
        'arquivo': 'agendamentos.csv',
        'processador': Agendamento,
        'registros': []
    },
    'cliente': {
        'arquivo': 'clientesEstabelecimento.csv',
        'processador': Cliente,
        'registros': []
    },
    'produto': {
        'arquivo': 'produtos.csv',
        'processador': Produto,
        'registros': []
    },
    'profissional': {
        'arquivo': 'profissionais.csv',
        'processador': Produto,
        'registros': []
    },
    'servicos': {
        'arquivo': 'servicosDoEstabelecimento.csv',
        'processador': Servico,
        'registros': []
    }
}


def processa_elemento(nome_elemento):
    path_arquivo = f'{path_arquivos}{os.sep}{mapa_arquivo_processador[nome_elemento]["arquivo"]}'
    with open(path_arquivo) as f:
        linhas = f.readlines()
        primeira_linha = True
        contador_linha = 1
        for linha in linhas:
            if primeira_linha:
                primeira_linha = False
                continue

            proc = mapa_arquivo_processador[nome_elemento]['processador']
            obj = proc.processa_linha_csv(linha, contador_linha)

            if obj is not None:
                # Realiza o tratamento dos dados
                obj.trata_dados()
                # Se houver um mapeamento para o DW, será persistido no banco
                obj.gera_registro_dw()
                mapa_arquivo_processador[nome_elemento]['registros'].append(obj)
                contador_linha += 1


def gera_fato_pagamento():
    pass


def main():
    for item in mapa_arquivo_processador:
        processa_elemento(item)
    gera_fato_pagamento()


if __name__ == '__main__':
    main()
