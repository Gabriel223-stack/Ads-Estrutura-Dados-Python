class Node:
    def __init__(self, valor):  # Corrigido o nome do método
        self.valor = valor
        self.proximo = None
        
class ListaLigada:
    def __init__(self):
        self.cabeca = None
        
    def mostrar(self):
        atual = self.cabeca
        pos = 0
        while atual:
            print(f"Posição {pos} | Nó atual: [{atual.valor}] (id: {id(atual)}) -> Próximo: {id(atual.proximo) if atual.proximo else None}")
            atual = atual.proximo
            pos += 1
        print("Fim da lista \n")
        
    def inserir_ordenado(self, valor):  # Corrigido o nome do método
        novo_no = Node(valor)
        
        if self.cabeca is None or valor < self.cabeca.valor:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
            return 
        
        atual = self.cabeca
        while atual.proximo and atual.proximo.valor < valor:
            atual = atual.proximo
            
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no

# --- Criando a lista e inserindo valores ---
lista = ListaLigada()
lista.inserir_ordenado(3)
lista.inserir_ordenado(10)
lista.inserir_ordenado(20)
lista.inserir_ordenado(1)
lista.inserir_ordenado(25)
lista.inserir_ordenado(5)

# --- Mostrando a lista ---
lista.mostrar()
