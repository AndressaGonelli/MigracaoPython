from typing import List
from models.Cliente import Cliente
from pyodbc import Error
from service.serviceODBC import ServiceODBC


class ServiceCliente:
    @staticmethod
    def cadastrar(linha, args):

        endereco = [item for item in args if item.id == linha["ENDERECO_ID"]]
        cliente = Cliente(
            linha["ID"],
            linha["NOME"],
            endereco[0],
            linha["CPF_CNPJ"],
            linha["CREDITO"],
            linha["TELEFONE"],
            linha["EMAIL"],
            linha["ATIVO"]
        )
        return cliente

    @staticmethod
    def criarTabelaDB():
        try:
            cursor, conn = ServiceODBC.openConection()

            if(ServiceODBC.checkIfTableExists("CLIENTES")):
                print("Tabela CLIENTES já existe")
            else:
                sql_command='''
                CREATE TABLE CLIENTES(
                ID INT PRIMARY KEY,
                NOME VARCHAR(200) NOT NULL,
                ENDERECO_ID INT NOT NULL,
                CPF_CNPJ VARCHAR(15) NOT NULL,
                CREDITO FLOAT NOT NULL,
                TELEFONE VARCHAR(15) NOT NULL,
                EMAIL VARCHAR(100),
                ATIVO BIT NOT NULL,
                CONSTRAINT FK_ENDERECO FOREIGN KEY (ENDERECO_ID) REFERENCES ENDERECOS(ID));
                '''
                cursor.execute(sql_command)
                conn.commit()
                print("Tabela CLIENTES criada com sucesso no Banco de Dados")
        except Error as e:
            print(f'Falha ao criar tabela CLIENTES:{str(e)}')
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def inserirBD(clientes:List[Cliente]):
        try:
            cursor, conn = ServiceODBC.openConection()

            insert_query = ''' INSERT INTO CLIENTES( ID,NOME, ENDERECO_ID, CPF_CNPJ,CREDITO, TELEFONE, EMAIL, ATIVO) \
                                VALUES(?,?,?,?,?,?,?,?);'''

            for c in clientes:
                values = (c.id, c.nome,c.endereco.id, c.cpf,c.credito,c.telefone,c.email,c.ativo)

                cursor.execute(insert_query,values)
            conn.commit()
            print("Dados inseridos com sucesso na tabela CLIENTES no Banco de Dados")

            
        except Error as e:
            print(f'Falha ao gravar registros na tabela CLIENTES:{str(e)}')
        finally:
            cursor.close()
            conn.close()