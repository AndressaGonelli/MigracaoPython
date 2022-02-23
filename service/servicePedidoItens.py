from typing import List
from models.PedidoItens import Pedido_Itens
from pyodbc import Error
from service.serviceODBC import ServiceODBC

class ServicePedidoItens:
    @staticmethod
    def cadastrar(linha, args):

        produto = [item for item in args['produtos'] if item.id == linha["PRODUTO_ID"]]
        pedido = [item for item in args['pedidos'] if item.id == linha["PEDIDO_ID"]]

        pedido_item = Pedido_Itens(
            linha["ID"],
            pedido[0],
            produto[0],
            linha["QUANTIDADE"],
            linha["PRECO_UNITARIO"],
            linha["PRECO_TOTAL"]
        )
        return pedido_item
    
    @staticmethod
    def criarTabelaDB():
        try:
            cursor, conn = ServiceODBC.openConection()

            if(ServiceODBC.checkIfTableExists("PEDIDOS_ITENS")):
                print("Tabela PEDIDOS_ITENS já existe")
            else:
                sql_command='''
                CREATE TABLE PEDIDOS_ITENS(
                ID INT PRIMARY KEY,
                PRODUTO_ID INT NOT NULL,
                PEDIDO_ID INT NOT NULL,
                QUANTIDADE INT NOT NULL,
                PRECO_UNITARIO FLOAT NOT NULL,
                PRECO_TOTAL FLOAT NOT NULL,
                CONSTRAINT FK_PRODUTO FOREIGN KEY (PRODUTO_ID) REFERENCES PRODUTOS(ID),
                CONSTRAINT FK_PEDIDO FOREIGN KEY (PEDIDO_ID) REFERENCES PEDIDOS(ID));
                '''
                cursor.execute(sql_command)
                conn.commit()
                print("Tabela PEDIDOS_ITENS criada com sucesso no Banco de Dados")

        except Error as e:
            print(f'Falha ao criar tabela PEDIDOS_ITENS:{str(e)}')
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def inserirBD(pedidos_itens:List[Pedido_Itens]):
        try:
            cursor, conn = ServiceODBC.openConection()

            insert_query = ''' INSERT INTO PEDIDOS_ITENS (ID, PRODUTO_ID, PEDIDO_ID, QUANTIDADE, PRECO_UNITARIO,PRECO_TOTAL)  \
                                VALUES(?,?,?,?,?,?);'''

            for p in pedidos_itens:
                values = (p.id, p.produto.id, p.pedido.id, p.quantidade, p.preco_unitario, p.preco_total)

                cursor.execute(insert_query,values)
            conn.commit()
            print("Dados inseridos com sucesso na tabela PEDIDOS_ITENS no Banco de Dados")
            
        except Error as e:
            print(f'Falha ao gravar registros na tabela PEDIDOS_ITENS:{str(e)}')
        finally:
            cursor.close()
            conn.close()