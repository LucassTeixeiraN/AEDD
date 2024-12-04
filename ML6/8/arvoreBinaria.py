from estudante import Estudante
from node import No

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, estudante):
        if self.raiz is None:
            self.raiz = No(estudante)
        else:
            self._inserir_recursivo(self.raiz, estudante)

    def _inserir_recursivo(self, no, estudante):
        if estudante.codigo < no.estudante.codigo:
            if no.esquerda is None:
                no.esquerda = No(estudante)
            else:
                self._inserir_recursivo(no.esquerda, estudante)
        else:
            if no.direita is None:
                no.direita = No(estudante)
            else:
                self._inserir_recursivo(no.direita, estudante)

    def buscar_mais_alto(self):
        return self._buscar_mais_alto(self.raiz)

    def _buscar_mais_alto(self, no):
        if no is None:
            return None
        maior_altura = no.estudante
        if no.esquerda:
            estudante_esquerda = self._buscar_mais_alto(no.esquerda)
            if estudante_esquerda and estudante_esquerda.altura > maior_altura.altura:
                maior_altura = estudante_esquerda
        if no.direita:
            estudante_direita = self._buscar_mais_alto(no.direita)
            if estudante_direita and estudante_direita.altura > maior_altura.altura:
                maior_altura = estudante_direita
        return maior_altura

    def buscar_mais_velho(self):
        return self._buscar_mais_velho(self.raiz)

    def _buscar_mais_velho(self, no):
        if no is None:
            return None
        mais_velho = no.estudante
        if no.esquerda:
            estudante_esquerda = self._buscar_mais_velho(no.esquerda)
            if estudante_esquerda and estudante_esquerda.idade > mais_velho.idade:
                mais_velho = estudante_esquerda
        if no.direita:
            estudante_direita = self._buscar_mais_velho(no.direita)
            if estudante_direita and estudante_direita.idade > mais_velho.idade:
                mais_velho = estudante_direita
        return mais_velho

    def mostrar_maiores_de_idade(self):
        return self._mostrar_maiores_de_idade(self.raiz)

    def _mostrar_maiores_de_idade(self, no):
        if no is None:
            return []
        estudantes = []
        if no.estudante.idade >= 18:
            estudantes.append(no.estudante)
        estudantes += self._mostrar_maiores_de_idade(no.esquerda)
        estudantes += self._mostrar_maiores_de_idade(no.direita)
        return estudantes

    def buscar_maior_media(self):
        return self._buscar_maior_media(self.raiz)

    def _buscar_maior_media(self, no):
        if no is None:
            return None
        maior_media = no.estudante
        if no.esquerda:
            estudante_esquerda = self._buscar_maior_media(no.esquerda)
            if estudante_esquerda and estudante_esquerda.media_academica > maior_media.media_academica:
                maior_media = estudante_esquerda
        if no.direita:
            estudante_direita = self._buscar_maior_media(no.direita)
            if estudante_direita and estudante_direita.media_academica > maior_media.media_academica:
                maior_media = estudante_direita
        return maior_media

    def buscar_menor_media(self):
        return self._buscar_menor_media(self.raiz)

    def _buscar_menor_media(self, no):
        if no is None:
            return None
        menor_media = no.estudante
        if no.esquerda:
            estudante_esquerda = self._buscar_menor_media(no.esquerda)
            if estudante_esquerda and estudante_esquerda.media_academica < menor_media.media_academica:
                menor_media = estudante_esquerda
        if no.direita:
            estudante_direita = self._buscar_menor_media(no.direita)
            if estudante_direita and estudante_direita.media_academica < menor_media.media_academica:
                menor_media = estudante_direita
        return menor_media
