import sys

try:
    parametro = sys.argv

    if parametro[1] == '-f':
        open('wordlist.txt', 'w')

    else:
        wordlist = open(str(parametro[1]), 'r+')

    try:
        for i in range(int(parametro[2])):
            wordlist.write(str(parametro[3]) + str(i) + '\n')

    except FileNotFoundError:
        print('selecione um arquivo!')
    
except IndexError:
    print('''
    GERADOR DE WORDLIST

    EXMPLO: gerador-dowdilist.py <seleciona aquivo em texto> <gerado de numero> <argumentos>    
    
    -f CRIA UM ARQUIVO DE TEXTE LIMPO 

    ''')