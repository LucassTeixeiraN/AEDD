''' Faça um programa que cadastre n produtos. Para cada produto devem ser
cadastrados código do produto, preço e quantidade estocada. Os dados devem ser
armazenados em uma lista simplesmente encadeada e não ordenada. Posteriormente,
receber do usuário a taxa de desconto (ex.: digitar 10 para taxa de desconto de 10%).
Aplicar a taxa digitada ao preço de todos os produtos cadastrados e finalmente
mostrar um relatório com o código e o novo preço. O final desse relatório deve
apresentar também a quantidade de produtos com quantidade estocada superior a
500.'''
from listProduct import ListProduct

def main():
    lista_produtos = ListProduct()
    
    n = int(input("Quantos produtos deseja cadastrar? "))
    if n > 0:
        i = 0
        while n > 0:
            i = i + 1
            try:
                codigo = int(input(f"Digite o código do produto {i}: "))
                preco = float(input(f"Digite o preço do produto {i}: R$ "))
                quantidade = int(input(f"Digite a quantidade estocada do produto {i}: \n"))
                lista_produtos.cadastrar_produto(codigo, preco, quantidade)
                n -= 1
            except ValueError:
                print("Dados inválidos.")

    taxa_desconto = float(input("\nDigite a taxa de desconto (em %): \n"))
    
    lista_produtos.aplicar_desconto(taxa_desconto)
    
    lista_produtos.relatorio_produtos()

main()