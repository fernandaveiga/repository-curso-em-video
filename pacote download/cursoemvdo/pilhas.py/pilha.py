class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#inserir da pilha
#remover da pilha
#observar o topo da pilha

class Stack:
    def __init__(self):
        self.top = None #não há elemento no topo, pois não há nenhum elemento
        self._size = 0 #tamanho da lista inicia em 0
    
    def push(self, elem):
        #insere um elemento elem na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size +1

    def pop(self):
        #remove o elemento do topo da pilha
        if self._size>0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node
        raise IndexError('The stack is empty')

    def peek(self):
        # retorna o topo sem remover
        if self._size >0:
            return self.top
        raise IndexError('The stack is empty')
    
    def __len__(self):
        #retorna o tamanho da lista
        return self._size
    
    def __repr__(self):
        #exibiro que tem dentro da pilha
        r = ''
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + '\n'
            pointer = pointer.next
        return r

pilha = Stack()
pilha.push(4)
pilha.push('ava')
pilha.push(12)
print(pilha)
pilha.pop()
print('-'*30)
print(pilha)
print('-'*30)
pilha.pop()
pilha.pop()
pilha.pop()