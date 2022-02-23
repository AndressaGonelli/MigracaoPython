from dataclasses import dataclass, field
from sqlite3 import Date
from models.Cliente import Cliente

@dataclass(order=True)  #frozen = True -> cria read only objects 
class Pedido:
    sort_index:int = field(init=False, repr=False) #init = false -> ele não é exigido no construtor,
    id:int 
    data:Date                                         # e repr=false faz que ele não apareça por default no print do objeto 
    cliente:Cliente
    valor_total:float
    valor_pago:float
    desconto:float = 0

    def __post_init_(self):
        self.sort_index = self.id
        #object.__setattr__(self, 'sort_index', self.id) forma dde fazer atribuição caso a class esteja frozen

    def __str__(self):
        return f'{self.desconto},{self.valor_total}' #exibição personalizada de quando der print do objeto     

    #var = 'abcde'
    #print(f"frase: {var!r}")
    #->frase: 'abcde'