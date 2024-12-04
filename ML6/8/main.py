'''Faça um programa para executar as operações abaixo em uma árvore binária
ordenada pelo código, onde o dado não seja um inteiro, mas uma estrutura contendo
dados de um estudante: código, nome, idade, altura e média acadêmica.
Menu
1 – Inserir estudante
2 – Mostrar o estudante mais alto
3 – Mostrar o estudante mais velho
4 – Mostrar os estudantes maiores de idade
5 – Mostrar o estudante com maior média acadêmica
6 – Mostrar o estudante com menor média acadêmica
7 – Sair'''
# main.py
from arvoreBinaria import ArvoreBinaria
from estudante import Estudante

def menu():
        print("\nMenu:")
        print("1 – Inserir estudante")
        print("2 – Mostrar o estudante mais alto")
        print("3 – Mostrar o estudante mais velho")
        print("4 – Mostrar os estudantes maiores de idade")
        print("5 – Mostrar o estudante com maior média acadêmica")
        print("6 – Mostrar o estudante com menor média acadêmica")
        print("7 – Sair")
  
        opcao = input("Escolha uma opção: ")
        
        return opcao
    
def main():
    arvore = ArvoreBinaria()
    while True:
        if input("\nPressione ENTER para ir ao Menu.") == '':
            try:
                opcao = menu()
                if opcao == "1":
                    codigo = int(input("Código do estudante: "))
                    nome = input("Nome do estudante: ")
                    idade = int(input("Idade do estudante: "))
                    altura = float(input("Altura do estudante (em metros): "))
                    media_academica = float(input("Média acadêmica do estudante: "))

                    estudante = Estudante(codigo, nome, idade, altura, media_academica)
                    arvore.inserir(estudante)
                    print(f"Estudante {nome} inserido com sucesso!")

                elif opcao == "2":
                    estudante = arvore.buscar_mais_alto()
                    if estudante:
                        print(f"Estudante mais alto: {estudante}")
                    else:
                        print("Não há estudantes na árvore.")

                elif opcao == "3":
                    estudante = arvore.buscar_mais_velho()
                    if estudante:
                        print(f"Estudante mais velho: {estudante}")
                    else:
                        print("Não há estudantes na árvore.")

                elif opcao == "4":
                    estudantes = arvore.mostrar_maiores_de_idade()
                    if estudantes:
                        print("Estudantes maiores de idade:")
                        for estudante in estudantes:
                            print(estudante)
                    else:
                        print("Não há estudantes maiores de idade na árvore.")

                elif opcao == "5":
                    estudante = arvore.buscar_maior_media()
                    if estudante:
                        print(f"Estudante com maior média acadêmica: {estudante}")
                    else:
                        print("Não há estudantes na árvore.")

                elif opcao == "6":
                    estudante = arvore.buscar_menor_media()
                    if estudante:
                        print(f"Estudante com menor média acadêmica: {estudante}")
                    else:
                        print("Não há estudantes na árvore.")

                elif opcao == "7":
                    print("Saindo do programa.")
                    break

                else:
                    print("Opção inválida. Tente novamente.")
            except(ValueError):
                print("Erro ao inserir estudante. Por favor, verifique os dados.")
if __name__ == "__main__":
    main()
