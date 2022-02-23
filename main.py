from service.serviceDados import ServiceDados
from service.serviceODBC import ServiceODBC
from models.Endereco import Endereco

dict_tabelas = {}

dict_tabelas['enderecos'] = []
dict_tabelas['clientes'] = []
dict_tabelas['fornecedores'] = []
dict_tabelas['produtos'] = []
dict_tabelas['pedidos'] = []
dict_tabelas['itensPedidos'] = []


while True:
    print("==========================")
    print("Escolha a opção")
    print("1 - Testar conexão com banco de dados")
    print("2 - Criar estruturas de tabela no banco de dados")
    print("3 - Apagar todos as tabelas do Banco de dados\n")


    print("4 - Carregar dados via csv")
    print("5 - Apagar dados carregados")
    print("6 - Sumarizar dados carregados\n")

    print("7 - Inserir no banco de dados os dados carregados")
    print("8 - Sumarizar dados salvos no Banco de dados")
    print("9 - Apagar todos os dados do Banco de dados")
    print("10 - Sair")
    print("==========================\n")
    opcao = int(input())

     
    if opcao == 1:  # Conectar banco de dados
        ServiceODBC.testConnection()
    elif opcao == 2:  # Criar estruturas de tabela
        ServiceDados.criarTabelasDB()
    elif opcao == 3: # Apagar todos as tabelas do Banco de dados
        ServiceODBC.dropAllTables()
    elif opcao == 4:# Carregar dados do CSV
        dict_tabelas = ServiceDados.carregarDoCSV()
    elif opcao == 5:# Apagar dados carregados
        dict_tabelas = ServiceDados.apagarDadosCarregados(dict_tabelas)
    elif opcao == 6:# Sumarizar dados carregados
        ServiceDados.Sumarizar(dict_tabelas)
    elif opcao == 7:# Inserir no banco de dados os dados carregados
        ServiceDados.inserirNasTabelasDB(dict_tabelas)
    elif opcao == 8:# Sumarizar dados salvos no Banco de dados
        ServiceDados.SumarizarDB()
    elif opcao == 9:# Apagar todos os dados do Banco de dados
        ServiceODBC.deleteAllTables()
    elif opcao == 10:
        break
    else:
        print("\nOpção inválida\n")
