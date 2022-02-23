from typing import List
from models.Pedido import Pedido
from pyodbc import Error
from service.serviceODBC import ServiceODBC

class ServicePedido:
    @staticmethod
    def cadastrar(linha, args):

        cliente = [item for item in args if item.id == linha["CLIENTE_ID"]]
        pedido = Pedido(
            linha["ID"],
            linha["Data"],
            cliente[0],
            linha["VALOR_TOTAL"],
            linha["VALOR_PAGO"],
            linha["DESCONTO"]
        )
        return pedido
    
    @staticmethod
    def criarTabelaDB():
        try:
            cursor, conn = ServiceODBC.openConection()

            if(ServiceODBC.checkIfTableExists("PEDIDOS")):
                print("Tabela PEDIDOS já existe")
            else:
                sql_command='''
                CREATE TABLE PEDIDOS(
                ID INT PRIMARY KEY,
                DATA DATETIME,
                CLIENTE_ID INT NOT NULL,
                VALOR_TOTAL FLOAT NOT NULL,
                DESCONTO FLOAT,
                VALOR_PAGO FLOAT NOT NULL,
                CONSTRAINT FK_CLIENTE FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTES(ID));
                '''
                cursor.execute(sql_command)
                conn.commit()
                print("Tabela PEDIDOS criada com sucesso no Banco de Dados")

        except Error as e:
            print(f'Falha ao criar tabela PEDIDOS:{str(e)}')
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def inserirBD(pedidos:List[Pedido]):
        try:
            cursor, conn = ServiceODBC.openConection()

            insert_query = ''' INSERT INTO PEDIDOS (ID, DATA, CLIENTE_ID, VALOR_TOTAL, DESCONTO, VALOR_PAGO) \
                                VALUES(?,?,?,?,?,?);'''

            for p in pedidos:
                values = (p.id, p.data, p.cliente.id, p.valor_total, p.desconto, p.valor_pago)

                cursor.execute(insert_query,values)
            conn.commit()
            print("Dados inseridos com sucesso na tabela PEDIDOS no Banco de Dados")
            
        except Error as e:
            print(f'Falha ao gravar registros na tabela PEDIDOS:{str(e)}')
        finally:
            cursor.close()
            conn.close()