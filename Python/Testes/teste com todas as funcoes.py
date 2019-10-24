situacao = ''
while situacao != '5':
    #situação inicial do sistema:
    print('1) entrar com os dados da aeronave')
    print('2) calculadora')
    print('3) -')
    print('4) -')
    print('5) sair do sistema')
    print()

    situacao = input('Situação: ')

    if situacao == '5':
        print('saindo do sistema')
        break

    #caso a opção escolhida seja 1, seguira para a adição dos dados da aeronave
    #em seguida dará mais duas opções, que são:
    #analisar a situação da aeronave ou voltar ao início
    while situacao == '1':

        aeronave = {'aeronave': input('Aeronave: '), 'hdv': float(input('Horas de voo: ')), 'ultima lubrificacao': float(input('Horas desde a ultima lubrificação: '))}
        print()
        print('1) Situação da aeronave')
        print('2) voltar ao inicio')
        subsituacao = input('entrada: ')
        
        #se a opção escolhida for 1, fará a analise da situação da aeronave:
        if subsituacao == '1':
            #analise pelas horas de voo:
            if (aeronave['hdv'] < 250):
                print()
                print(aeronave['aeronave'], 'não necessita de manutenção devido a horas de voo', sep=' ')
            else:
                print()
                print(aeronave['aeronave'], 'necessita de manutenção devido a horas de voo', sep = ' ')

            #analise pela lubrificação
            if aeronave['ultima lubrificacao'] < 50:
                print(aeronave['aeronave'], 'não necessita de lubrificação', sep= ' ')
                print()
                print('voltando ao inicio')
                print('...')
                print()    
                break
            else:
                print(aeronave['aeronave'], 'necessita de lubrificação', sep= ' ')
                print()
                print('voltando ao início')
                print('...')
                print()
                break

        #se a opção escolhida for 2 retornará ao inicio:
        if subsituacao == '2':
            print()
            print('voltando para o inicio')
            print('...')
            print()
            break

    #se a opção escolhida for 2, iniciará o modo calculadora
    if situacao == '2':
        
        print('Bem vindo a calculadora, favor inserir os valores que devem ser calculados')
        
        x = float(input('x: '))
        y = float(input('y: '))
        operacao = input('operação: ')
        #operações:
        def somar(x,y):
            return(x+y)
        def subtrair(x,y):
            return(x-y)
        def multiplicar(x,y):
            return(x*y)
        def dividir(x,y):
            return(x/y)
        def expoente(x,y):
            return(x**y)
        def radical(x,y):
            return(x**(1/y))

        #impressão do resultado:
        if operacao == '+':
            print()
            print('resultado:')
            print(somar(x,y))
            print()
        if operacao =='-':
            print()
            print('resultado:')
            print(subtrair(x,y))
            print()
        if operacao == '*':
            print()
            print('resultado:')
            print(multiplicar(x,y))
            print()
        if operacao =='/':
            print()
            print('resultado:')
            print(dividir(x,y))
            print()
        if operacao == '^':
            print()
            print('resultado:')
            print(expoente(x,y))
            print()
        if operacao =='raiz':
            print()
            print('resultado:')
            print(radical(x,y))
            print()

    #situação 3, quiz game show
    while situacao == '3':
        print()
        print('bem vindo ao quiz')
        print('1) quantas aeronaves se apresentam numa apresentação padrão da esquadrilha da fumaça?')
        r = input('resposta: ')
        if r == '7':
            print('resposta correta!!! proxima pergunta:')
            print()
            print('Quais aeronaves formam uma dupla separada da equipe?')
            s = input('resposta: ')

            if s == '5 e 6':
                print()
                print('resposta correta!!! Proxima pergunta:')
                print()
                print('qual o lar da esquadrilha da fumaça?')
                t = input('resposta: ')

                if t == 'Pirassununga':
                    print()
                    print('resposta correta!!! Proxima pergunta:')
                    print()
                    print('Qual a abreviação do nome original da esquadrilha da fumaça?')
                    u = input('resposta: ')

                elif t == 'pirassununga':
                    print()
                    print('resposta correta!!! Proxima pergunta:')
                    print()
                    print('Qual a abreviação do nome original da esquadrilha da fumaça?')
                    u = input('resposta: ')

                    if u =='Eda':
                        print()
                        print('resposta correta!!! Proxima pergunta:')
                        print()
                        print('qual é a aeronave utilizada pela esquadrilha da fumaça?')
                        v = input('resposta: ')
                    elif u == 'EDA':
                        print()
                        print('resposta correta!!! Proxima pergunta:')
                        print()
                        print('qual é a aeronave utilizada pela esquadrilha da fumaça?')
                        v = input('resposta: ')
                    elif u =='eda':
                        print()
                        print('resposta correta!!! Proxima pergunta:')
                        print()
                        print('qual é a aeronave utilizada pela esquadrilha da fumaça?')
                        v = input('resposta: ')

                        if v == 'A29':
                            print()
                            print('resposta correta!!! Proxima pergunta:')
                            print()
                            print('você chegou ao fim do quiz, parabéns!!!')
                            print()
                            break
                        elif v == 'a29':
                            print()
                            print('resposta correta!!! Proxima pergunta:')
                            print()
                            print('você chegou ao fim do quiz, parabéns!!!')
                            print()
                            break
                        elif v == 'super tucano':
                            print()
                            print('resposta correta!!! Proxima pergunta:')
                            print()
                            print('você chegou ao fim do quiz, parabéns!!!')
                            print()
                            break
                        elif v == 'a-29':
                            print()
                            print('resposta correta!!! Proxima pergunta:')
                            print()
                            print('você chegou ao fim do quiz, parabéns!!!')
                            print()
                            break
                        elif v == 'A-29':
                            print()
                            print('resposta correta!!! Proxima pergunta:')
                            print()
                            print('você chegou ao fim do quiz, parabéns!!!')
                            print()
                            break

                        else:
                            print()
                            print('resposta errada! começe novamente!')
                            break

                    else:
                        print()
                        print('resposta errada! começe novamente!')
                        break

                else:
                    print()
                    print('resposta errada! começe novamente!')
                    break

            elif s == '5 6':
                print()
                print('resposta correta!!! Proxima pergunta:')
                print()
                print('qual o lar da esquadrilha da fumaça?')
                t = input('resposta: ')
            elif s == '5, 6':
                print()
                print('resposta correta!!! Proxima pergunta:')
                print()
                print('qual o lar da esquadrilha da fumaça?')
                t = input('resposta: ')
            elif s == '5,6':
                print()
                print('resposta correta!!! Proxima pergunta:')
                print()
                print('qual o lar da esquadrilha da fumaça?')
                t = input('resposta: ')
            elif s =='56':
                print()
                print('resposta correta!!! Proxima pergunta:')
                print()
                print('qual o lar da esquadrilha da fumaça?')
                t = input('resposta: ')

                if t == 'Pirassununga':
                    print()
                    print('resposta correta!!! Proxima pergunta:')
                    print()
                    print('Qual a abreviação do nome original da esquadrilha da fumaça?')
                    u = input('resposta: ')

                elif t == 'pirassununga':
                    print()
                    print('resposta correta!!! Proxima pergunta:')
                    print()
                    print('Qual a abreviação do nome original da esquadrilha da fumaça?')
                    u = input('resposta: ')

                    if u =='Eda':
                        print()
                        print('resposta correta!!! Proxima pergunta:')
                        print()
                        print('qual é a aeronave utilizada pela esquadrilha da fumaça?')
                        v = input('resposta: ')
                    elif u == 'EDA':
                        print()
                        print('resposta correta!!! Proxima pergunta:')
                        print()
                        print('qual é a aeronave utilizada pela esquadrilha da fumaça?')
                        v = input('resposta: ')
                    elif u =='eda':
                        print()
                        print('resposta correta!!! Proxima pergunta:')
                        print()
                        print('qual é a aeronave utilizada pela esquadrilha da fumaça?')
                        v = input('resposta: ')

                        if v == 'A29':
                            print()
                            print('resposta correta!!! Proxima pergunta:')
                            print()
                            print('você chegou ao fim do quiz, parabéns!!!')
                            print()
                            break
                        elif v == 'a29':
                            print()
                            print('resposta correta!!! Proxima pergunta:')
                            print()
                            print('você chegou ao fim do quiz, parabéns!!!')
                            print()
                            break
                        elif v == 'super tucano':
                            print()
                            print('resposta correta!!! Proxima pergunta:')
                            print()
                            print('você chegou ao fim do quiz, parabéns!!!')
                            print()
                            break
                        elif v == 'a-29':
                            print()
                            print('resposta correta!!! Proxima pergunta:')
                            print()
                            print('você chegou ao fim do quiz, parabéns!!!')
                            print()
                            break
                        elif v == 'A-29':
                            print()
                            print('resposta correta!!! Proxima pergunta:')
                            print()
                            print('você chegou ao fim do quiz, parabéns!!!')
                            print()
                            break

                        else:
                            print()
                            print('resposta errada! começe novamente!')
                            break

                    else:
                        print()
                        print('resposta errada! começe novamente!')
                        break

                else:
                    print()
                    print('resposta errada! começe novamente!')
                    break

            else:
                print()
                print('resposta errada! começe novamente!')
                break

        else:
            print()
            print('resposta errada! começe novamente!')
            break
    #situação 4 ainda não definida
    if situacao == '4':
        print()
        print('ainda não definido')
        print('voltando para o início')
        print('...')
        print()
