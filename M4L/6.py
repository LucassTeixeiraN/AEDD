
# 6. Faça um programa que cadastre n funcionários. Para cada funcionário devem ser
# cadastrados nome e salário. Os dados devem ser armazenados em uma lista
# simplesmente encadeada e ordenada, de forma decrescente, pelo salário do
# funcionário. Posteriormente, o programa de mostrar:
# a. O nome do funcionário que tem o maior salário (em caso de empate mostrar
# todos);
# b. A média salarial de todos os funcionários juntos;
# c. A quantidade de funcionários com salário superior a um valor fornecido pelo
# usuário. Caso nenhum funcionário satisfaça essa condição, mostrar
# mensagem.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.proximo = None  


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_ordenado(self, nome, salario):
        novo_funcionario = Funcionario(nome, salario)

        if self.cabeca is None or self.cabeca.salario >= salario:
            novo_funcionario.proximo = self.cabeca
            self.cabeca = novo_funcionario
        else:
            atual = self.cabeca
            while atual.proximo is not None and atual.proximo.salario < salario:
                atual = atual.proximo
            novo_funcionario.proximo = atual.proximo
            atual.proximo = novo_funcionario

    def exibir(self):
        atual = self.cabeca
        while atual is not None:
            print(f"Nome: {atual.nome}, Salário: {atual.salario}")
            atual = atual.proximo

    def calcular_media_salarial(self):
        total_salario = 0
        contador = 0
        atual = self.cabeca
        while atual is not None:
            total_salario += atual.salario
            contador += 1
            atual = atual.proximo
        return total_salario / contador if contador > 0 else 0

    def funcionarios_maior_salario(self):
        if self.cabeca is None:
            return []

        maior_salario = self.cabeca.salario
        atual = self.cabeca
        while atual is not None:
            if atual.salario > maior_salario:
                maior_salario = atual.salario
            atual = atual.proximo

    
        funcionarios_maior = []
        atual = self.cabeca
        while atual is not None:
            if atual.salario == maior_salario:
                funcionarios_maior.append(atual.nome)
            atual = atual.proximo

        return funcionarios_maior

    def contar_funcionarios_acima_de(self, valor):
        contador = 0
        atual = self.cabeca
        while atual is not None:
            if atual.salario > valor:
                contador += 1
            atual = atual.proximo
        return contador

def main():
    lista_funcionarios = ListaEncadeada()
    n = int(input("Quantos funcionários deseja cadastrar? "))

    for _ in range(n):
        nome = input("Digite o nome do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))
        lista_funcionarios.inserir_ordenado(nome, salario)

    print("\nFuncionários cadastrados em ordem de salário:")
    lista_funcionarios.exibir()

    media_salarial = lista_funcionarios.calcular_media_salarial()
    print(f"\nMédia salarial de todos os funcionários: {media_salarial:.2f}")

    funcionarios_maior_salario = lista_funcionarios.funcionarios_maior_salario()
    print("\nFuncionário(s) com o maior salário:")
    for nome in funcionarios_maior_salario:
        print(nome)

    valor = float(input("\nDigite o valor para verificar salários superiores: "))
    quantidade_acima = lista_funcionarios.contar_funcionarios_acima_de(valor)
    if quantidade_acima > 0:
        print(f"\nQuantidade de funcionários com salário acima de {valor}: {quantidade_acima}")
    else:
        print(f"\nNenhum funcionário possui salário acima de {valor}.")

main()

