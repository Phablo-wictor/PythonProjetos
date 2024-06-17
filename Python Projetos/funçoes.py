import sys

def tem_sete_letras(argumentos):
    if  len(argumentos) == 7:
        return True

    else:
        return False
    
argu = sys.argv

if tem_sete_letras(argu[1]):
    print('relmete tem 7 letras')

else:
    print('nao tem 7 letras')


