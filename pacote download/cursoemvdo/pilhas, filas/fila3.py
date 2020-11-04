class Filas():
    def __init__(self):
        self.data1 = []
        self.data2 = []
    
    def inserir(self,x):
        if x >=60:
            return self.data1.append(x)
        else:
            return self.data2.append(x)

    def remover(self):
        if len(self.data1)>0 and len(self.data2)>0:
            return self.data1.pop(0) and self.data2.pop(0)
        else:
            return self.data1.pop(0) or self.data2.pop(0)

fila = Filas()
fila.inserir(3)
fila.inserir(4)
fila.inserir(12)
fila.inserir(5)
fila.inserir(60)
fila.inserir(65)
fila.remover()
