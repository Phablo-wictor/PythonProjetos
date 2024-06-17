
def coresResistor3():
    try:
        valoresResistor = []
        NuFaxa = ['PRIMEIRA FAXA!','SEGUNDA FAXA','TERCEIRA FAXA']
        for i in NuFaxa:

                print(i)

                print('\n','SELECINA AS CORES DO RESISTOR!')
                
                cores = int(input(' Preto(0) \n Marrom(1) \n Vermelho(2) \n Laranja(3) \n Amarelo(4) \n Verde(5) \n Azul(6) \n Violetar(7) \n cinza(8) \n Branco(9) \n'))

                if cores == 0:
                    valoresResistor.append(0)

                elif cores == 1:
                    valoresResistor.append(1)

                elif cores == 2:
                    valoresResistor.append(2)

                elif cores == 3:
                    valoresResistor.append(3)

                elif cores == 4:
                    valoresResistor.append(4)

                elif cores == 5:
                    valoresResistor.append(5)

                elif cores == 6:
                    valoresResistor.append(6)

                elif cores == 7:
                    valoresResistor.append(7)

                elif cores == 8:
                    valoresResistor.append(8)

                elif cores == 9:
                    valoresResistor.append(9)
                
                else:
                    print('Opção Ivalida')

    except ValueError:
        print('opição invalida!')

    except IndexError:
        print('Opição Invalida!')

    else:
        for i in range(valoresResistor[2]):
            valoresResistor.append(0)
            
        del valoresResistor[2]
        print('Resutado:')
        for x in valoresResistor:
            print(x,end='')

        print(' Ω \n')





def coresResistor4():
    try:
        valoresResistor = []
        NuFaxa = ['PRIMEIRA FAXA!','SEGUNDA FAXA','TERCEIRA FAXA','QUAL É A TOLERÂNCIA!']
        for i in NuFaxa:

            if i == 'QUAL É A TOLERÂNCIA!':
                print(i)
                tole = int(input('(1)DOURADO! (0)PRATA!'))

                if tole == 1:
                    print('Dourado! selecionado!')

                if tole == 0:
                    print('Prata! selecionado!')

            else:

                print(i)

                print('\n','SELECINA AS CORES DO RESISTOR!')
                
                cores = int(input(' Preto(0) \n Marrom(1) \n Vermelho(2) \n Laranja(3) \n Amarelo(4) \n Verde(5) \n Azul(6) \n Violetar(7) \n cinza(8) \n Branco(9) \n'))

                if cores == 0:
                    valoresResistor.append(0)

                elif cores == 1:
                    valoresResistor.append(1)

                elif cores == 2:
                    valoresResistor.append(2)

                elif cores == 3:
                    valoresResistor.append(3)

                elif cores == 4:
                    valoresResistor.append(4)

                elif cores == 5:
                    valoresResistor.append(5)

                elif cores == 6:
                    valoresResistor.append(6)

                elif cores == 7:
                    valoresResistor.append(7)

                elif cores == 8:
                    valoresResistor.append(8)

                elif cores == 9:
                    valoresResistor.append(9)
                
                else:
                    print("Opção Invalida")

    except ValueError:
        print('opição invalida!')

    except IndexError:
        print('Opição Invalida!')

    else:
        for i in range(valoresResistor[2]):
            valoresResistor.append(0)
            
        del valoresResistor[2]
        print('Resultado:')
        for x in valoresResistor:
            print(x,end='')

        print(' Ω \n')

def coresResistor5():
    try:
        valoresResistor = []
        NuFaxa = ['PRIMEIRA FAXA!','SEGUNDA FAXA','TERCEIRA FAXA','QUARTA FAIXA','QUAL É TOLERANCIA!']
        for i in NuFaxa:

            if i == 'QUAL É TOLERANCIA!':
                print(i)
                tole = int(input('(1)DOURADO! (0)PRATA!'))

                if tole == 1:
                    print('Dourado! selecionado!')

                if tole == 0:
                    print('Prata! selecionado!')

            else:

                print(i)

                print('\n','SELECINA AS CORES DO RESISTOR!')
                
                cores = int(input(' Preto(0) \n Marrom(1) \n Vermelho(2) \n Laranja(3) \n Amarelo(4) \n Verde(5) \n Azul(6) \n Violetar(7) \n cinza(8) \n Branco(9) \n'))

                if cores == 0:
                    valoresResistor.append(0)

                elif cores == 1:
                    valoresResistor.append(1)

                elif cores == 2:
                    valoresResistor.append(2)

                elif cores == 3:
                    valoresResistor.append(3)

                elif cores == 4:
                    valoresResistor.append(4)

                elif cores == 5:
                    valoresResistor.append(5)

                elif cores == 6:
                    valoresResistor.append(6)

                elif cores == 7:
                    valoresResistor.append(7)

                elif cores == 8:
                    valoresResistor.append(8)

                elif cores == 9:
                    valoresResistor.append(9)

                else:
                    print('OPIÇAO INVALIDA!')
                    break

    except ValueError:
        print('opição invalida!')
    
    except IndexError:
        print('OPIÇÃO INVALIDA!')

    else:
        for i in range(valoresResistor[3]):
            valoresResistor.append(0)
            
        del valoresResistor[3]
        print('Resultado:')
        for x in valoresResistor:
            print(x,end='')
        
        print(' Ω\n')
        
while True:
    try:
        faxa =  int(input('Quantas faixas tem o seu resistor? \n (3)faixa \n (4)faixa \n (5)fixa \n (0)Saír \n'))

        if faxa == 3:
            coresResistor3()

        elif faxa == 4:
            coresResistor4()
        
        elif faxa == 5:
            coresResistor5()
        
        elif faxa == 0:
            break
      
    except ValueError:
        print('OPIÂO INVALIDA!')