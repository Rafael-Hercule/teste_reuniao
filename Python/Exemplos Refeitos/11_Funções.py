# Funções

x = 2
y = 3
def somar(x, y):
    resultado = x+y
    return resultado
print('Soma: ' + str(somar(x,y)))

def subtrair(x,y):
    return(y-x)
print('Subtração: ' + str(subtrair(x,y)))

def multiplicar(x, y):
    return(x*y)
print('Multiplicação: ' + str(multiplicar(x,y)))

def dividir(x,y):
    return(y/x)
print('Divisão: ' + str(dividir(x,y)))

def x_quadrado(x):
    return(x**2)
print('x²: ' + str(x_quadrado(x)))

def y_quadrado(y):
    return(y**2)
print('y²: ' + str(y_quadrado(y)))

def soma_dos_quadrados(x,y):
    return((x**2)+(y**2))
print('x² + y²: ' + str(soma_dos_quadrados(x,y)))

def x_elevado_a_y(x,y):
    return(x**y)
print('x^y: ' + str(x_elevado_a_y(x,y)))

def y_elevado_a_x(x,y):
    return(y**x)
print('y^x: ' + str(y_elevado_a_x(x,y)))

def raiz_x(x):
    return(x**(1/2))
print(raiz_x(x))

def raiz_y(y):
    return(y**(1/2))
print(raiz_y(y))
