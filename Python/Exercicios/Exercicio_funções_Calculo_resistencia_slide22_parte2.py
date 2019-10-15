#Funções

#informações sobre o circuito
r1 = float(input('r1 = '))
r2 = float(input('r2 = '))
montagem = input('motagem = ')

#para Paralelo
def p(r1,r2):
    return((r1*r2)/(r1+r2))
#para em serie
def s(r1,r2):
    return(r1+r2)

#impressão condicional
if montagem == 'p':
    print( 'r1 = ' + str(r1)+ '; ' + 'r2 = ' + str(r2) + ' '+ 'calculo_resistência = '  +  str(p(r1,r2)) +  '; ' + 'Montagem: ' + montagem)

elif montagem == 's':
    print('r1 = ' + str(r1)+ '; ' + 'r2 = ' + str(r2) + ' '+ 'calculo_resistência = '  +  str(s(r1,r2)) +  '; ' + 'Montagem: ' + montagem)
