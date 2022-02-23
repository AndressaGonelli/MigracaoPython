from genericpath import exists
from tkinter import filedialog
from tkinter import Tk
import pandas as pd
from pyodbc import Error

from service.serviceCliente import ServiceCliente
from service.serviceEndereco import ServiceEndereco
from service.serviceFornecedor import ServiceFornecedor
from service.servicePedido import ServicePedido
from service.serviceProduto import ServiceProduto
from service.servicePedidoItens import ServicePedidoItens
from service.serviceODBC import ServiceODBC


class ServiceDados:

    @staticmethod
    def carregarDoCSV():
        try:
            enderecos = ServiceDados.criarObjetoDoCSV(
                "ENDEREÇOS", ServiceEndereco, None)

            clientes = ServiceDados.criarObjetoDoCSV(
                "CLIENTES", ServiceCliente, enderecos)

            fornecedores = ServiceDados.criarObjetoDoCSV(
                "FORNECEDORES", ServiceFornecedor, enderecos)

            produtos = ServiceDados.criarObjetoDoCSV(
                "PRODUTOS", ServiceProduto, fornecedores)

            pedidos = ServiceDados.criarObjetoDoCSV(
                "PEDIDOS", ServicePedido, clientes)

            itensPedido = ServiceDados.criarObjetoDoCSV("ITENS DO PEDIDO", ServicePedidoItens, {
                'pedidos': pedidos, 'produtos': produtos})
           
            return {'enderecos': enderecos, 'clientes': clientes, 'fornecedores': fornecedores, 'produtos': produtos, 'pedidos': pedidos, 'itensPedidos': itensPedido}

        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")

    @staticmethod
    def criarObjetoDoCSV(tipo, service, args):
        data = [("Arquivo CSV(*.csv)", "*.csv")]
        input(
            f"Pressione ENTER para selecionar o arquivo CSV que contém os {tipo}")
        caminho = filedialog.askopenfilename(
            title=f"Selecione o CSV de {tipo}", filetypes=data)

        if exists(caminho):
            itens = []
            df = pd.read_csv(caminho, header=0, keep_default_na=False)
            for index, line in df.iterrows():
                itens.append(service.cadastrar(line, args))
            print(
                f"Os {len(itens)} registros de {tipo} foram cadastrados com sucesso")
            return itens
        else:
            print(
                f"Falha no arquivo de {tipo}. Caminho ou arquivo informado não existe. Tente novamente")
            return None

    @staticmethod
    def apagarDadosCarregados(dict_tabelas):

        dict_tabelas['endereco'] = []
        dict_tabelas['clientes'] = []
        dict_tabelas['fornecedores'] = []
        dict_tabelas['produtos'] = []
        dict_tabelas['pedidos'] = []
        dict_tabelas['itensPedidos'] = []

        return dict_tabelas

    @staticmethod
    def Sumarizar(dict_tabelas):
        print(f"\nHá {len(dict_tabelas['enderecos'])} endereços cadastrados")
        print(f"Há {len(dict_tabelas['clientes'])} clientes cadastrados")
        print(
            f"Há {len(dict_tabelas['fornecedores'])} fornecedores cadastrados")
        print(f"Há {len(dict_tabelas['produtos'])} produtos cadastrados")
        print(f"Há {len(dict_tabelas['pedidos'])} pedidos cadastrados")
        print(
            f"Há {len(dict_tabelas['itensPedidos'])} itens de pedidos cadastrados\n")

    @staticmethod
    def criarTabelasDB():

        ServiceEndereco.criarTabelaDB()
        ServiceCliente.criarTabelaDB()
        ServiceFornecedor.criarTabelaDB()
        ServiceProduto.criarTabelaDB()
        ServicePedido.criarTabelaDB()
        ServicePedidoItens.criarTabelaDB()

    @staticmethod
    def inserirNasTabelasDB(dict_tabelas):

        ServiceEndereco.inserirBD(dict_tabelas['enderecos'])
        ServiceCliente.inserirBD(dict_tabelas['clientes'])
        ServiceFornecedor.inserirBD(dict_tabelas['fornecedores'])
        ServiceProduto.inserirBD(dict_tabelas['produtos'])
        ServicePedido.inserirBD(dict_tabelas['pedidos'])
        ServicePedidoItens.inserirBD(dict_tabelas['itensPedidos'])

    @staticmethod
    def SumarizarDB():
        try:

            tables = ['PEDIDOS_ITENS', 'PEDIDOS', 'PRODUTOS',
                      'CLIENTES', 'FORNECEDORES', 'ENDERECOS']

            for item in tables:

                if ServiceODBC.checkIfTableExists(item):

                    sqlcommand = f'''
                        SELECT COUNT(ID)QTD FROM [dbo].[{item}];
                    '''
                    cursor, conn = ServiceODBC.openConection()
                    r = cursor.execute(sqlcommand)
                    row = r.fetchone()
                    print(f'Há {row[0]} registros na tabela {item}')
                    cursor.close()
                    conn.close()
                else:
                    print(f'Tabela {item}  não existe no banco de dados')

        except Error as e:
            print(f"Erro ao sumarizar dados do banco de dados : {str(e)}")
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")
