import sys
argumentos = sys.argv

def soma(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2 


if argumentos[1] == 'soma':
    resutado = soma(float(argumentos[2]), float(argumentos[3]))
    print(resutado)

elif argumentos[1] == 'sub':
    respota = sub(float(argumentos[2]), float(argumentos[3]))
    print(respota)

