class Estudante:
    def __init__(self, codigo, nome, idade, altura, media_academica):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.media_academica = media_academica

    def __str__(self):
        return f"{self.codigo} - {self.nome}, Idade: {self.idade}, Altura: {self.altura}m, Média Acadêmica: {self.media_academica}"

    def __repr__(self):
        return self.__str__()
