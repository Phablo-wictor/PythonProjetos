lista = []
from os import system

while True:

    opicao = input('Voce deseja fazer?\n[i]nserir [a]pagar [l]ista: ')

    if opicao == 'i' or opicao == 'I':
        system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        

    elif opicao == 'a' or opicao == 'A':
        try:
            apagar = int(input('Qual indice voce desja apagar: '))
         
            print(f'O íten {lista[apagar]} foi apagado com sucesso')
            del lista[apagar]
        except ValueError:
            print('Digite numeros inteiro')
        
        except IndexError:
            print('ídice ivalido!')
      
            
    elif opicao == 'l' or opicao == 'L':
        for indice, nome in enumerate(lista):
             print(indice, nome)

    else: 
        system('cls')
        print('Opição Ivalida!!')
       