# implementar um programa de gerenciamento de dua filas em um banco:prioritária e normal
# Seu programa deverá permitir que pessoas sejam inscritas no fim de cada fila, dependendo da idade de cada uma (acima de 60 anos entra na fila proritária).
# A saída de pessoas da fila deve ocorrer da seguinte forma: a cada duas pessoas que saem da fila prioritária, uma sai da fila normal
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
            return self.data1.pop(0), self.data1.pop(0), self.data2.pop(0)
        elif len(self.data1)>0 and len(self.data2)==0:
            return self.data1.pop(0)
        elif len(self.data2)>0 and len(self.data1)==0:
            return self.data2.pop(0)
        else:
            pass

fila = Filas()
fila.inserir(3)
fila.inserir(4)
fila.inserir(12)
fila.inserir(5)
fila.inserir(60)
fila.inserir(65)
print(fila.remover())
