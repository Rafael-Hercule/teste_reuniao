# Definindo Classes
class Aeronave:
    def __init__(self, modelo):
        self.modelo = modelo
    def imprimir(self):
        print(self.modelo)

aeronave_1 = Aeronave('F-4')
aeronave_2 = Aeronave('F-5')
aeronave_3 = Aeronave('F-15')
aeronave_4 = Aeronave('F-16')
aeronave_5 = Aeronave('F-18')
aeronave_6 = Aeronave('F-22')
aeronave_7 = Aeronave('F-35')

aeronave_1.imprimir()
aeronave_3.imprimir()
