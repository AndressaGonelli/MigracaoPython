from dataclasses import dataclass
from models.Fornecedor import Fornecedor

@dataclass
class Produto:
     id:int
     nome:str
     fornecedor: Fornecedor
     preco_custo:float
     preco_venda:float
     categoria:str
     ativo:int
   
        