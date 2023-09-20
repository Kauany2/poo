class Carro:
    def __init__(self,cor,modelo):
        self.cor=cor
        self.modelo=modelo

    def acelerar(self):
        print(f"O {self.modelo} está acelerando!")

    def frear(self):
        print(f"O {self.modelo} está freando!")

    def ligar_farois(self):
        self.farois_ligados = True
        print("Faróis ligados!")

    def desligar_farois(self):
        self.farois_ligados = False
        print("Faróis desligados!")

    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor

meu_carro=Carro('vermelho','Fusca')
meu_carro.ligar_farois()
print(meu_carro.farois_ligados)
meu_carro.desligar_farois()

meu_carro.set_cor("rosa")
print(meu_carro.get_cor())

print(meu_carro.cor)
print(meu_carro.modelo)

meu_carro.acelerar()
meu_carro.frear()