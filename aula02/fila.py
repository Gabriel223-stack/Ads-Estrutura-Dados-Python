import random
import os

class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileira(self):
        novo = No(random.randint(0, 99))
        if self.inicio is None:
            self.inicio = novo
        else:
            self.fim.prox = novo
        self.fim = novo
        print("Elemento enfileirado com sucesso!")

    def desenfileira(self):
        if self.inicio is not None:
            ptr = self.inicio
            dado = ptr.dado
            self.inicio = ptr.prox
            if self.inicio is None:
                self.fim = None  # Fila vazia
            return dado
        else:
            print("Fila vazia!")
            return -1

    def mostrar(self):
        limpar_tela()
        print("Elementos da fila:")
        if self.inicio is None:
            print("Fila vazia.")
        else:
            atual = self.inicio
            while atual is not None:
                print(atual.dado, end=" ")
                atual = atual.prox
            print()

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    f = Fila()
    while True:
        print("\n--- MENU ---")
        print("1 - Enfileirar")
        print("2 - Desenfileirar")
        print("3 - Mostrar fila")
        print("4 - Sair")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        if opcao == 1:
            f.enfileira()
        elif opcao == 2:
            valor = f.desenfileira()
            if valor != -1:
                print(f"Elemento desenfileirado: {valor}")
        elif opcao == 3:
            f.mostrar()
        elif opcao == 4:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamada para iniciar o menu
menu()
