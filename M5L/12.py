
# 12. Faça um programa que apresente o menu de opções abaixo:
# MENU
# 1- Cadastrar tipo
# 2- Cadastrar produto
# 3- Consultar o preço de um produto
# 4- Excluir tipo
# 5- Sair
# Observações:
# a. Mostrar mensagem de opção inválida do menu. A opção 5 é a única que sai do
# programa.
# b. Para a implementação do programa acima, é necessário utilizar duas filas.
# c. Na primeira fila serão armazenados os tipos de produtos com seus respectivos
# percentuais de impostos. Verifique que todos os tipos sejam diferentes e cada
# tipo é identificado com apenas uma letra.
# d. Na segunda fila serão armazenados os produtos cujo número deve ser gerado
# automaticamente. O preço e o tipo devem ser digitados. Lembrando que um
# produto só pode ser cadastrado se for de um tipo também já cadastrado. Faça
# essa verificação.
# e. Na primeira opção do menu serão cadastrados os tipos, um de cada vez: cada
# vez que o usuário escolhe a opção 1 do menu, ele tem a possibilidade de
# cadastrar um novo tipo (letra que representa o tipo e percentual de imposto).
# Nesta opção, a única mensagem disponível é: Tipo cadastrado.
# f. Na segunda opção do menu serão cadastrados os produtos, um de cada vez:
# cada vez que o usuário escolhe a opção 2 do menu, ele tem a possibilidade de
# cadastrar um novo produto (número gerado automaticamente, preço e tipo
# digitados). Lembrando que um produto só pode ser cadastrado se o tipo ao
# qual ele pertence já existe na fila de tipos. Nesta opção, as mensagens
# disponíveis são: Produto cadastrado e Tipo de produto inexistente.
# g. Na terceira opção do menu, o usuário digita o número do produto que deseja
# consultar o preço e, se este existir na fila de produtos, o programa deve
# procurar por seu percentual de imposto, de acordo com o tipo do produto na
# fila de tipos, calcular e mostrar seu preço, ou seja, preço cadastrado menos o
# percentual de imposto. Nesta opção, as mensagens disponíveis são: Preço =
# valor calculado, Produto não cadastrado e Fila vazia.
# h. Na quarta opção, o programa deve excluir um tipo da fila de tipos, respeitando
# a forma de organização de uma fila. Lembrando que um tipo só pode ser
# excluído se não existir nenhum produto cadastrado para ele.

from collections import deque

tipos = deque()
produtos = deque()
produto_id = 1

def cadastrar_tipo():
    tipo = input("Digite a letra que representa o tipo: ").upper()
    if any(t['tipo'] == tipo for t in tipos):
        print("Tipo já cadastrado.")
        return
    percentual = float(input("Digite o percentual de imposto: "))
    tipos.append({'tipo': tipo, 'percentual': percentual})
    print("Tipo cadastrado.")

def cadastrar_produto():
    global produto_id
    preco = float(input("Digite o preço do produto: "))
    tipo = input("Digite o tipo do produto: ").upper()
    if not any(t['tipo'] == tipo for t in tipos):
        print("Tipo de produto inexistente.")
        return
    produtos.append({'id': produto_id, 'preco': preco, 'tipo': tipo})
    produto_id += 1
    print("Produto cadastrado.")

def consultar_preco():
    if not produtos:
        print("Fila vazia.")
        return
    numero = int(input("Digite o número do produto: "))
    produto = next((p for p in produtos if p['id'] == numero), None)
    if not produto:
        print("Produto não cadastrado.")
        return
    tipo = next((t for t in tipos if t['tipo'] == produto['tipo']), None)
    if not tipo:
        print("Tipo de produto não cadastrado.")
        return
    preco_final = produto['preco'] * (1 + tipo['percentual'] / 100)
    print(f"Preço = {preco_final:.2f}")

def excluir_tipo():
    if not tipos:
        print("Fila vazia.")
        return
    tipo = tipos.popleft()
    if any(p['tipo'] == tipo['tipo'] for p in produtos):
        print("Não é possível excluir um tipo com produtos cadastrados.")
        tipos.appendleft(tipo)
        return
    print("Tipo excluído.")

def menu():
    while True:
        print("\nMENU")
        print("1- Cadastrar tipo")
        print("2- Cadastrar produto")
        print("3- Consultar o preço de um produto")
        print("4- Excluir tipo")
        print("5- Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_tipo()
        elif opcao == '2':
            cadastrar_produto()
        elif opcao == '3':
            consultar_preco()
        elif opcao == '4':
            excluir_tipo()
        elif opcao == '5':
            print('Encerrando...')
            break
        else:
            print("Opção inválida.")
menu()
