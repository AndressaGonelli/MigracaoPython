from dataclasses import dataclass
from models.Endereco import Endereco

@dataclass
class Cliente:
    id: int
    nome:str
    endereco:Endereco
    cpf:str
    credito:float
    telefone:str
    email:str
    ativo: int
   
