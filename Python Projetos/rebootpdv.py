from pyautogui import *
import time as t

alert('ATENÇÃO NÃO MEXA NO PC ATÉ QUE A OPERAÇÃO SEJÁ COMCLUIDA')

ipPDV = [119,148,122,141,130,116,106,105,153]


def ssh(ip):
    write(f'ssh root@192.168.49.{ip}')
    press('enter')
    t.sleep(3)
    write('yes')
    press('enter')



press('win')
write('cmd')
press('enter')
t.sleep(1)

ssh(ipPDV[0])