class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    
    def push(self, elem):
        #insere um elemento elem na fila
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1

    def pop(self):
        #remove o elemento do topo da pilha0:
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem
        raise IndexError('The queue is empty')


    def peek(self):
        # retorna o topo sem remover
        if self._size>0:
            elem = self.first.data
            return elem
        raise IndexError('The queue is empty')

    
    def __len__(self):
        #retorna o tamanho da lista
        return self._size
    
    def __repr__(self):
        #representação visual do que tem dentro da pilha
        if self._size > 0:
            r = ''
            pointer = self.first
            while(pointer):
                r = r+ str(pointer.data) + ' '
                pointer = pointer.next
            return r
        return 'Empty Queue'

fila = Queue()
print(fila)
fila.push('queuque')
fila.push(5)
fila.push('ola')
print(fila)
