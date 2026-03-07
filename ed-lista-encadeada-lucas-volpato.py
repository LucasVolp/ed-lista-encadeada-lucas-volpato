# Implemente uma Lista Encadeada Simples em Python, conforme discutido em aula.

# A implementação deve utilizar classes próprias para representar:

# Node → representa cada nó da lista

# LinkedList → representa a lista encadeada

# Cada nó deve armazenar:

# um valor (data)

# uma referência para o próximo nó (next)

# Métodos obrigatórios

# Sua implementação deve conter, no mínimo, os seguintes métodos:

# insert_beginning(value) — inserir elemento no início da lista
# insert_end(value) — inserir elemento no final da lista
# remove(value) — remover um elemento da lista
# search(value) — buscar um elemento na lista
# print_list() — imprimir os elementos da lista
# size() — retornar o tamanho da lista
# is_empty() — verificar se a lista está vazia

# Entrega da atividade

# A entrega será realizada enviando o link do repositório GitHub no Moodle.

# Cada aluno deverá criar um repositório público contendo a implementação da atividade.

# Nome do repositório

# Utilize o seguinte padrão:

# ed-lista-encadeada-nome-sobrenome
# Exemplo:
# ed-lista-encadeada-joao-silva


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

no1 = Node(3)
no2 = Node(5)
no3 = Node(2)

no1.next = no2
no2.next = no3

# print(no1.next.next.data)


# ---- 

class LinkedList:
    def __init__(self):
        self.head = None # Lista Vázia
        self._size = 0

    def insert_beginning(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self._size += 1
    
    def insert_end(self, value):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(value)
        else:
            self.head = Node(value)
        self._size += 1

    def remove(self, value):
        if self.head:
            pointer = self.head
            prev = None
            while pointer.next:
                if pointer.data == value:
                    if prev is None:
                        self.head = pointer.next
                    else: 
                        prev.next = pointer.next
                    self._size -= 1
                    return True
                prev = pointer
                pointer = pointer.next
            return False
        
li = LinkedList()
li.insert_end(1)
li.insert_end(2)
li.insert_end(3)




            


    