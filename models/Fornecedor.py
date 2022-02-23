from dataclasses import dataclass
from models.Endereco import Endereco

@dataclass
class Fornecedor:
    id:int
    razao_social:str
    fantasia:str
    cnpj:str
    endereco:Endereco
