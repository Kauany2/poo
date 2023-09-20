class Triangulo:
    def __init__(self):
        self.ladoA = int(input("Digite o lado A: "))
        self.ladoB = int(input("Digite o lado B: "))
        self.ladoC = int(input("Digite o lado C: "))

    def perimetro(self):
        p = self.ladoA + self.ladoB + self.ladoC
        print("O perímetro é: ", p)

    def maior_lado(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            print("O número maior é: ", self.ladoA)

        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            print("O número maior é: ", self.ladoB)

        elif self.ladoC > self.ladoB and self.ladoC > self.ladoA:
            print("O número maior é: ", self.ladoC)

    def lado_max(self):
        lados = [self.ladoA, self.ladoB, self.ladoC]
        print("O maior lado é: ", max(lados))

t = Triangulo()
t.perimetro()
t.maior_lado()
t.lado_max()