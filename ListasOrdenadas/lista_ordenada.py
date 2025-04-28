from node import Node

class ListaOrdenada:
    def __init__(self):
        self.head = None

    def inserir_ordenado(self, data):
        novo_no = Node(data)
        if self.head is None or self.head.data >= data:
            novo_no.next = self.head
            self.head = novo_no
        else:
            atual = self.head
            while atual.next and atual.next.data < data:
                atual = atual.next
            novo_no.next = atual.next
            atual.next = novo_no

