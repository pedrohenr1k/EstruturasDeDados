from node import Node

class ListaSimples:
    def __init__(self):
        self.head = None

    def inserir_inicio(self, data):
        novo_no = Node(data)
        novo_no.next = self.head
        self.head = novo_no

    def buscar(self, data):
        atual = self.head
        while atual:
            if atual.data == data:
                return True
            atual = atual.next
        return False

    def excluir(self, data):
        atual = self.head
        anterior = None
        while atual:
            if atual.data == data:
                if anterior:
                    anterior.next = atual.next
                else:
                    self.head = atual.next
                return True
            anterior = atual
            atual = atual.next
        return False
