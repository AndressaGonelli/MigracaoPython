from dataclasses import dataclass
from models.Produto import Produto
from models.Pedido import Pedido

@dataclass
class Pedido_Itens:
    id:int
    pedido:Pedido
    produto:Produto
    quantidade:float
    preco_unitario:float
    preco_total: float