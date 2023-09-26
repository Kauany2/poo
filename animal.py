class Animal:
    def __init__(self, nome, cor, raca, especie, habitat):
        self._nome = nome
        self._cor = cor
        self._raca = raca
        self._especie = especie
        self._habitat = habitat

class Cachorro(Animal):
    def __init__(self, nome, cor, raca, especie, habitat, som):
        super().__init__(nome, cor, raca, especie, habitat)
        self._som = som

