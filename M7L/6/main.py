'''Crie um programa para ler um grafo a partir de um arquivo e armazená-lo em uma
estrutura de lista de adjacência. Crie um formato para o seu arquivo de entrada.'''

from grafo import Grafo

def main():
    # Lê o grafo a partir de um arquivo
    nome_arquivo = 'grafo.txt'
    grafo = Grafo.ler_arquivo(nome_arquivo)
    
    # Exibe o grafo
    print("Lista de Adjacência do Grafo:")
    grafo.mostrar()

if __name__ == "__main__":
    main()
