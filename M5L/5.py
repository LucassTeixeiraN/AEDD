class Aviao:
    def __init__(self, nome, identificador, capacidade):
        self.nome = nome
        self.identificador = identificador
        self.capacidade = capacidade

    def __str__(self):
        return f"Nome: {self.nome} | ID: {self.identificador} | Capacidade: {self.capacidade} passageiros"

class Aeroporto:
    def __init__(self):
        self.fila_decolagem = []

    def listar_numero_avioes(self):
        print(f"\nNúmero de aviões na fila de decolagem: {len(self.fila_decolagem)}\n")

    def autorizar_decolagem(self):
        if self.fila_decolagem:
            aviao = self.fila_decolagem.pop(0)
            print(f"\nAvião autorizado para decolagem:\n  {aviao}\n")
        else:
            print("\nNenhum avião na fila de decolagem.\n")

    def adicionar_aviao(self, aviao):
        self.fila_decolagem.append(aviao)
        print(f"\nAvião adicionado à fila de espera:\n  {aviao}\n")

    def listar_avioes(self):
        if self.fila_decolagem:
            print("\nAviões na fila de espera:")
            for idx, aviao in enumerate(self.fila_decolagem, start=1):
                print(f"  {idx}. {aviao}")
            print()  
        else:
            print("\nNenhum avião na fila de espera.\n")

    def listar_primeiro_aviao(self):
        if self.fila_decolagem:
            print("\nPrimeiro avião na fila de decolagem:")
            print(f"  {self.fila_decolagem[0]}\n")
        else:
            print("\nNenhum avião na fila de decolagem.\n")

def main()
    aeroporto = Aeroporto()
    
    
    aeroporto.adicionar_aviao(Aviao("Boeing 737", 101, 180))
    aeroporto.adicionar_aviao(Aviao("Airbus A320", 102, 200))
    aeroporto.adicionar_aviao(Aviao("Embraer E195", 103, 124))
    
    
    print("Lista de operações do aeroporto:\n")
    print("lista de numero aviões:") + aeroporto.listar_numero_avioes()
    print("lista de aviões:") + aeroporto.listar_avioes()
    print("lista primeiro de avião:") + aeroporto.listar_primeiro_aviao()
    aeroporto.autorizar_decolagem()
    aeroporto.listar_avioes()
    aeroporto.listar_numero_avioes()
main()
