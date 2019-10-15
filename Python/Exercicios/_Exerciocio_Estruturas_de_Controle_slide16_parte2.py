#Lita das aeronaves (com horas de voo a ser inserida)
fabricante_1 = {'fabricante': 'Boeing', 'Horas_de_voo': float(input("Horas de Voo Boeing: "))}
fabricante_2 = {'fabricante': 'Bombardier', 'Horas_de_voo': float(input("Horas de Voo Bombardier: "))}
fabricante_3 = {'fabricante': 'Outros', 'Horas_de_voo': float(input("Horas de Voo Outros: "))}

#Impressão das Horas de Voo
print('Horas de Voo ' + fabricante_1['fabricante'] + ': ' + str(fabricante_1['Horas_de_voo']))
print('Horas de Voo ' + fabricante_2['fabricante'] + ': ' + str(fabricante_2['Horas_de_voo']))
print('Horas de Voo ' + fabricante_3['fabricante'] + ': ' + str(fabricante_3['Horas_de_voo']))


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
    print(fabricante_3['fabricante'] + ' ' + 'Não necessitam manutenção')
