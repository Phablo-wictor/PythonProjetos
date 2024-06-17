import turtle as t
from time import sleep

t.bgcolor('blue')

t.fillcolor('red')

linha = 50


while True:
    t.forward(linha)
    t.left(90)

    linha += 5

t.end_fill()

sleep(3)

t.done()