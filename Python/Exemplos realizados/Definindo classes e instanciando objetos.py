# Definindo Classes

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def escrever_nome(self):
        print(self.nome)

pessoa_1 = Pessoa("Pedro")
pessoa_2 = pessoa_1
pessoa_2.escrever_nome()
