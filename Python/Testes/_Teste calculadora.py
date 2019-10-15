# Lembrar de tranformar a informação de entrada em float
x = float(input("X = "))
operacao = (input("Operação = "))
y = float(input("Y = "))
dados = {'X': x,'operação': operacao, "Y": y}
print(dados)

def somar(x,y):
    return(x+y)


def multiplicar(x,y):
    return(x*y)

#quando transformado em numro inteiro no começo não é necessária a transformação na hora
#da função print

def dividir(x,y):
    return(x/y)


def subtrair(x,y):
    return(x-y)


def x_elevado_y(x,y):
    return(x**y)


def radical_de_x(x,y):
    return(x**(1/y))

#uso do if para definir qual operação será usada:

if (operacao == "+"):
    print('(x+y) = ' + str(somar(float(x),float(y))))


elif operacao == "*":
    print('(x*y) = ' + str(multiplicar(float(x),float(y))))

elif operacao =="/":
    print('(x/y) = ' + str(dividir(x,y)))

elif operacao == "-":
    print('(x-y) = ' + str(subtrair(x,y)))

elif operacao == "^":
    print('(x^y) = ' + str(x_elevado_y(x,y)))

        
elif operacao == "raiz":
    print('y√x = ' + str(radical_de_x(x,y)))
