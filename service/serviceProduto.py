from typing import List
from models.Produto import Produto
from pyodbc import Error
from service.serviceODBC import ServiceODBC

class ServiceProduto:
    @staticmethod
    def cadastrar(linha, args):

        fornecedor = [item for item in args if item.id == linha["FORNECEDOR_ID"]]
        produto = Produto(
            linha["ID"],
            linha["NOME"],
            fornecedor[0],
            linha["PRECO_CUSTO"],
            linha["PRECO_VENDA"],
            linha["CATEGORIA"],
            linha["ATIVO"]
        )
        return produto

    @staticmethod
    def criarTabelaDB():
        try:
            cursor, conn = ServiceODBC.openConection()

            if(ServiceODBC.checkIfTableExists("PRODUTOS")):
                print("Tabela PRODUTOS já existe")
            else:
                sql_command='''
                CREATE TABLE PRODUTOS(
                ID INT PRIMARY KEY,
                NOME VARCHAR(100) NOT NULL,
                FORNECEDOR_ID INT NOT NULL,
                PRECO_CUSTO FLOAT NOT NULL,
                PRECO_VENDA FLOAT NOT NULL,
                CATEGORIA VARCHAR(100),
                ATIVO BIT NOT NULL,
                CONSTRAINT FK_FORNECEDOR FOREIGN KEY (FORNECEDOR_ID) REFERENCES FORNECEDORES(ID));
                '''
                cursor.execute(sql_command)
                conn.commit()
                print("Tabela PRODUTOS criada com sucesso no Banco de Dados")

        except Error as e:
            print(f'Falha ao criar tabela PRODUTOS:{str(e)}')
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def inserirBD(produtos:List[Produto]):
        try:
            cursor, conn = ServiceODBC.openConection()

            insert_query = ''' INSERT INTO PRODUTOS (ID, NOME, FORNECEDOR_ID, PRECO_CUSTO, PRECO_VENDA, CATEGORIA, ATIVO)  \
                                VALUES(?,?,?,?,?,?,?);'''

            for p in produtos:
                values = (p.id, p.nome, p.fornecedor.id, p.preco_custo, p.preco_venda, p.categoria, p.ativo)

                cursor.execute(insert_query,values)
            conn.commit()
            print("Dados inseridos com sucesso na tabela PRODUTOS no Banco de Dados")
            
        except Error as e:
            print(f'Falha ao gravar registros na tabela PRODUTOS:{str(e)}')
        finally:
            cursor.close()
            conn.close()