class Fila():
    def __init__(self):
        self.data = []
    
    def inserir(self,x):
        #inserir um elemento à direita, ao final da lista
        self.data.append(x)
    
    def remover(self):
        #remover o primeiro elemento da lista, de indice 0
        if len(self.data) > 0:
            return self.data.pop(0)
    
    def top(self):
        #consultar o primeiro elemento da lista
        if len(self.data) > 0:
            return self.data[0]
    
    def empty(self):
        return not len(self.data)>0

f = Fila()
f.inserir(3)
f.inserir(7)
f.inserir(9)
f.inserir(5)
print(f.remover())