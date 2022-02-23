from dataclasses import dataclass

@dataclass
class Endereco:
    id: int
    logradouro:str
    numero:int
    complemento:str
    cep:str
    bairro:str
    estado:str
    referencia:str
    regiao:str
    ativo: int
    