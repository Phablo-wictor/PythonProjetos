
lista = []

def add_tarefa():
    terefa = input("o que voce quer fazer hoje!")
    lista.append(terefa)
    return lista

n1 = 0

while (n1 < 50) :
    n1 = n1 + 1
    add_tarefa()

    for i in lista:
        print(str(n1) + i)