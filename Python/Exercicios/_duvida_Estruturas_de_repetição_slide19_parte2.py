#Lita das aeronaves (com horas de voo a ser inserida)
fabricante_1 = {'fabricante': 'Boeing', 'Horas_de_voo': float(input("Horas de Voo Boeing: "))}
fabricante_2 = {'fabricante': 'Bombardier', 'Horas_de_voo': float(input("Horas de Voo Bombardier: "))}
fabricante_3 = {'fabricante': 'Outros', 'Horas_de_voo': float(input("Horas de Voo Outros: "))}



#Exercicio slide 19 parte 2
situacao = ''
while(situacao != 'nenhum'):

    if float(fabricante_1['Horas_de_voo']) > 250:
        print('Efetuar Manutenção ' + fabricante_1['fabricante'])
    else:
        print(fabricante_1['fabricante'] + ' ' + 'Não necessita manutenção')

    if float(fabricante_2['Horas_de_voo']) > 180:
        print('Efetuar Manutenção ' + fabricante_2['fabricante'])
    else:
        print(fabricante_2['fabricante'] + ' ' + 'Não necessita manutenção')

    if float(fabricante_3['Horas_de_voo']) > 150:
        print('Efetuar Manutenção ' + fabricante_3['fabricante'])
    else:
        print(fabricante_3['fabricante'] + ' ' + 'Não necessitam manutenção')

    #parte retirada e movida para #*

#aqui é definido como parar o loop
    situacao = input('Situação: ')
    
    if situacao == 'nenhum':
        print('saindo do programa')
        break

    fabricante_1 = {'fabricante': 'Boeing', 'Horas_de_voo': float(input("Horas de Voo Boeing: "))}
    fabricante_2 = {'fabricante': 'Bombardier', 'Horas_de_voo': float(input("Horas de Voo Bombardier: "))}
    fabricante_3 = {'fabricante': 'Outros', 'Horas_de_voo': float(input("Horas de Voo Outros: "))}



#partes retiradas por não serem necessárias:
    #*
    '''if (fabricante_1['Horas_de_voo'] < 250):
        print(fabricante_1['fabricante'] + ' não necessita manutenção')
    elif (fabricante_2['Horas_de_voo'] < 180):
        print(fabricante_2['fabricante'] + ' não necessita manutenção')

    elif (fabricante_3['Horas_de_voo'] < 150):
        print(fabricante_3['fabricante'] + ' não necessita manutenção')
    '''


#essa parte foi colocada dentro do while
'''
#Impressão das Horas de Voo
print('Horas de Voo ' + fabricante_1['fabricante'] + ': ' + str(fabricante_1['Horas_de_voo']))
print('Horas de Voo ' + fabricante_2['fabricante'] + ': ' + str(fabricante_2['Horas_de_voo']))
print('Horas de Voo ' + fabricante_3['fabricante'] + ': ' + str(fabricante_3['Horas_de_voo']))

'''
'''
#Impressão se necessita ou não de manutenção
if float(fabricante_1['Horas_de_voo']) > 250:
    print('Efetuar Manutenção ' + fabricante_1['fabricante'])
else:
    print(fabricante_1['fabricante'] + ' ' + 'Não necessita manutenção')

if float(fabricante_2['Horas_de_voo']) > 180:
    print('Efetuar Manutenção ' + fabricante_2['fabricante'])
else:
    print(fabricante_2['fabricante'] + ' ' + 'Não necessita manutenção')

if float(fabricante_3['Horas_de_voo']) > 150:
    print('Efetuar Manutenção ' + fabricante_3['fabricante'])
else:
    print(fabricante_3['fabricante'] + ' ' + 'Não necessitam manutenção')'''


