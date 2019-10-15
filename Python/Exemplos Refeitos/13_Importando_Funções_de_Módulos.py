# Importando somente função pertencente ao módulo

from Funcoes import somar
print('x + y = ' + str(somar(4,5)))

from Funcoes import subtrair
print('y - x = ' + str(subtrair(4,5)))

from Funcoes import multiplicar
print('x * y = ' + str(multiplicar(4,5)))

from Funcoes import dividir
print('y / x = ' + str(dividir(4,5)))

from Funcoes import x_quadrado
print('x² = ' + str(x_quadrado(4)))

from Funcoes import y_quadrado
print('y² = ' + str(y_quadrado(5)))

