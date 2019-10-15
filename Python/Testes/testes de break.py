#Teste de Break

print('1) horas de voo', '2) horas desde ultima lubrificação', '3) situação geral', '4) sair do programa')


situacao = ''

while(situacao != 4):
    situacao = input('situação: ')
#condição para parar o programa:
    if(situacao == '4'):
        print('saindo do programa')
        break
    
    fabricante_1 = {'aeronave': input('aeronave: '), 'Horas_de_voo': float(input("Horas de Voo: ")), 'Ultima_Lubrificação': float(input('Horas desde a ultima lubrificação: '))}

#verificar apenas horas de voo:
    if situacao == '1':
        if (fabricante_1['Horas_de_voo'] < 250):
             print(fabricante_1['aeronave'], 'não necessita manutenção devido a horas de voo', sep=': ')
        else:
            print(fabricante_1['aeronave'], 'necessita manutenção', sep=': ')

#verificar apenas lubrificação:
    if situacao == '2':
        if( fabricante_1['Ultima_Lubrificação']) > 50:
            print(fabricante_1['aeronave'], 'necessita lubrificação', sep= ': ')
        else:
            print(fabricante_1['aeronave'], 'está com a lubrificação em dia', sep= ': ')

#verificar Horas de voo e Lubrificação:
    if situacao =='3':
        if (fabricante_1['Horas_de_voo'] < 250):
             print(fabricante_1['aeronave'], 'não necessita manutenção devido a horas de voo', sep=': ')
        else:
            print(fabricante_1['aeronave'], 'necessita manutenção', sep=': ')

        if( fabricante_1['Ultima_Lubrificação']) > 50:
            print(fabricante_1['aeronave'], 'necessita lubrificação', sep= ': ')
        else:
            print(fabricante_1['aeronave'], 'está com a lubrificação em dia', sep= ': ')
