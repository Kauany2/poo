'''class Teste1:
    a=1
    __b=2

class Teste2(Teste1):
    __c=3
    def __init__(self):
        print(self.a)
        print(self.__c)

t1 = Teste1()
print(t1.a)
'''

class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.nome= nome
        self.sexo= sexo
        self.cpf= cpf
        self.__ativo=ativo

    def desativar(self):
        self.__ativo= False
        print("A pessoa foi destivada com sucesso")

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

pessoa1= Pessoa("Joao", "M", "123456", True)
pessoa1.desativar()
pessoa1.set_nome("José")
print(pessoa1.get_nome())