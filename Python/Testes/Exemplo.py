aeronave = {'modelo': 'a320', 'fabricante': 'airbus', 'ano_fabric': 1995}
print(aeronave['modelo'])


#classe
class Aeronave:
    def __init__ (self, modelo):
        self.modelo = modelo
    def imprimir_modelo(self):
        print("o modelo dessa aeronave é: " + self.modelo)
#objeto
aeronave_1 = Aeronave('a320')
aeronave_2 = Aeronave('777')

aeronave_2.imprimir_modelo()
aeronave_1.imprimir_modelo()

print()

print(aeronave_1.modelo)
print(aeronave_2.modelo)

print()
#print() apenas para espaçar os conteudos
#lista

lista = [10, 20,30]
print(lista)
lista.pop()
print(lista)

print()

#.pop("objeto") retirar item selecionado caso não haja nenhum, o ultimo será retirado

#teste de classe
class Aviao_FAB:
    def __init__ (self, modelo):
        self.modelo = modelo
    def imprimir(self):
        print("O modelo da aeronave é: " + self.modelo)

aviao_1 = Aviao_FAB('F-5')
aviao_2 = Aviao_FAB('AMX-A1')
aviao_3 = Aviao_FAB('A-29 Super Tucano')
aviao_4 = Aviao_FAB('T-27 Tucano')
print(aviao_1.modelo)
print(aviao_2.modelo)
print(aviao_3.modelo)
print(aviao_4.modelo)
print()
#outro exemplo de .pop
#abtes do uso do .pop
print('antes do uso do .pop: ')
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(lista)

print()

#depois do uso do .pop
print('depois do uso do .pop: ')
lista.pop(0)
lista.pop(1)
lista.pop(2)
lista.pop(3)
lista.pop(4)
lista.pop(5)
print(lista)
