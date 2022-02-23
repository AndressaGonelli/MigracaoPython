from sqlite3 import Cursor
from typing import List
from models.Endereco import Endereco
from pandas import DataFrame
from service.serviceODBC import ServiceODBC
from pyodbc import Error

class ServiceEndereco:
    @staticmethod
    def cadastrar(linha: DataFrame, args):
        endereco = Endereco(
        linha["ID"],
        linha["LOGRADOURO"],
        linha["NUMERO"],
        linha["COMPLEMENTO"],
        linha["CEP"],
        linha["BAIRRO"],
        linha["ESTADO"],
        linha["REFERENCIA"],
        linha["REGIAO"],
        linha["ATIVO"])

        return endereco

    @staticmethod
    def criarTabelaDB():
        try:
            cursor, conn = ServiceODBC.openConection()

            if(ServiceODBC.checkIfTableExists("ENDERECOS")):
                print("Tabela ENDERECOS já existe")
            else:
                sql_command='''
                CREATE TABLE ENDERECOS(
                ID INT PRIMARY KEY,
                LOGRADOURO VARCHAR(100) NOT NULL,
                NUMERO  VARCHAR(10) NOT NULL,
                COMPLEMENTO  VARCHAR(100) NOT NULL,
                CEP  VARCHAR(8) NOT NULL,
                BAIRRO  VARCHAR(100) NOT NULL,
                ESTADO VARCHAR(2) NOT NULL,
                REFERENCIA  VARCHAR(100) NOT NULL,
                REGIAO VARCHAR(100) NOT NULL,
                ATIVO BIT NOT NULL);
                '''
                cursor.execute(sql_command)
                conn.commit()
                print("Tabela ENDERECOS criada com sucesso no Banco de Dados")

        except Error as e:
            print(f'Falha ao criar tabela ENDERECOS:{str(e)}')
        finally:
            cursor.close()
            conn.close()


    @staticmethod
    def inserirBD(enderecos:List[Endereco]):
        try:
            cursor, conn = ServiceODBC.openConection()

            insert_query = ''' INSERT INTO ENDERECOS (ID, LOGRADOURO, NUMERO, COMPLEMENTO, CEP, BAIRRO,ESTADO, \
                                REFERENCIA, REGIAO, ATIVO) \
                                VALUES(?,?,?,?,?,?,?,?,?,?);'''

            for e in enderecos:
                values = (e.id, e.logradouro,e.numero,e.complemento,e.cep,e.bairro,e.estado,e.referencia,e.regiao,e.ativo)

                cursor.execute(insert_query,values)
            conn.commit()
            print("Dados inseridos com sucesso na tabela ENDERECOS no Banco de Dados")
            
        except Error as e:
            print(f'Falha ao gravar registros na tabela ENDERECO:{str(e)}')
        finally:
            cursor.close()
            conn.close()



