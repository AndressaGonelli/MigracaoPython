
class Exemplo(): 
    def __init__(self,arquivo):
        self.arquivo = arquivo
        self.len = 0
    def ler(self):
        yield self.arquivo
        self.len +=1
        yield 0 
        self.len +=1
        yield 1 
        self.len +=1

 

a = Exemplo("aaa")
b = Exemplo("bbb").ler()
#print(a.len)

for i in a.ler() :
    print(i)

#print(getattr(a, 'len'))

for i in b :
    print(i)

for i in b :
    print(i)
