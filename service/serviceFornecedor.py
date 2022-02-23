from typing import List
from models.Fornecedor import Fornecedor
from service.serviceODBC import ServiceODBC
from pyodbc import Error

class ServiceFornecedor:
    @staticmethod
    def cadastrar(linha, args):

        endereco = [item for item in args if item.id == linha["ENDERECO_COBRANCA_ID"]]

        fornecedor = Fornecedor(
            linha["ID"],
            linha["RAZAO_SOCIAL"],
            linha["FANTASIA"],
            linha["CNPJ"],
            endereco[0]
        )
        return fornecedor
    @staticmethod
    def criarTabelaDB():
        try:
            cursor, conn = ServiceODBC.openConection()

            if(ServiceODBC.checkIfTableExists("FORNECEDORES")):
                print("Tabela FORNECEDORES já existe")
            else:
                sql_command='''
                CREATE TABLE FORNECEDORES(
                ID INT PRIMARY KEY,
                RAZAO_SOCIAL VARCHAR(200) NOT NULL,
                FANTASIA VARCHAR(200) NOT NULL,
                CNPJ VARCHAR(15) NOT NULL,
                ENDERECO_COBRANCA_ID INT NOT NULL,
                CONSTRAINT FK_ENDERECO_COBRANCA FOREIGN KEY (ENDERECO_COBRANCA_ID) REFERENCES ENDERECOS(ID));
                '''
                cursor.execute(sql_command)
                conn.commit()
                print("Tabela FORNECEDORES criada com sucesso no Banco de Dados")

        except Error as e:
            print(f'Falha ao criar tabela FORNECEDORES:{str(e)}')
        finally:
            cursor.close()
            conn.close()
    @staticmethod
    def inserirBD(fornecedores:List[Fornecedor]):
        try:
            cursor, conn = ServiceODBC.openConection()

            insert_query = ''' INSERT INTO FORNECEDORES (ID, RAZAO_SOCIAL, FANTASIA, CNPJ, ENDERECO_COBRANCA_ID) \
                                VALUES(?,?,?,?,?);'''

            for f in fornecedores:
                values = (f.id, f.razao_social,f.fantasia,f.cnpj,f.endereco.id)

                cursor.execute(insert_query,values)
            conn.commit()
            print("Dados inseridos com sucesso na tabela FORNECEDORES no Banco de Dados")
            
        except Error as e:
            print(f'Falha ao gravar registros na tabela FORNECEDORES:{str(e)}')
        finally:
            cursor.close()
            conn.close()
        