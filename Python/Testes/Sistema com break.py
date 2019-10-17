print('1) entrar com os dados da aeronave')
print('5) sair do sistema')

situacao = ''
while situacao != '5':

    situacao = input('Situação: ')

    if situacao == '5':
        print('saindo do sistema')
        break
        

    while situacao == '1':

        aeronave = {'aeronave': input('Aeronave: '), 'hdv': float(input('Horas de voo: ')), 'ultima lubrificacao': float(input('Horas desde a ultima lubrificação: '))}
        print('1) Situação da aeronave')
        print('2) voltar ao inicio')
        subsituacao = input('entrada: ')

        if subsituacao == '1':
            if (aeronave['hdv'] < 250):
                print(aeronave['aeronave'], 'não necessita de manutenção devido a horas de voo', sep=' ')
            else:
                print(aeronave['aeronave'], 'necessita de manutenção devido a horas de voo', sep = ' ')

            if aeronave['ultima lubrificacao'] < 50:
                print(aeronave['aeronave'], 'não necessita de lubrificação', sep= ' ')
            else:
                print(aeronave['aeronave'], 'necessita de lubrificação', sep= ' ')

        if subsituacao == '2':
            print('voltando para o inicio')
            print('1) entrar com os dados da aeronave')
            print('5) sair do sistema')
            break

    if situacao == '2':
        print('função ainda não definida')
        print('voltando ao início')
        print('1) entrar com os dados da aeronave')
        print('5) sair do sistema')

    if situacao == '3':
        print()

    if situacao == '4':
        print()
   
    
  
