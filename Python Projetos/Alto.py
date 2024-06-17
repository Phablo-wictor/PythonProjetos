from os import *
import webbrowser
from time import sleep
import pyautogui as py


while True:
    opicao = int(input("(1) Ativa a Licença\n(2)VisualCppRedist_AIO_x86_x64\n"))

    codico_ativacao = ('TX9XD-98N7V-6WMQ6-BX7FG-H8Q99', 'PVMJN-6DFY6-9CCP6-7BKTT-D3WVR'\
    , ' 7HNRX-D7KGG-3K4RQ-4WPJ4-', '3KHY7-WNT83-DGQKR-F7HPR-844BM', 'W269N-WFGWX-YVC9B-4J6C9-T83GX',\
    'MH37W-N47XK-V7XM9-C7227-GCQG9')

    if opicao == 1:
            opicao1 = int(input('Qual Sua Edição do Windows?\n(1)Home Core\n(2)Home/Core (Country Specific)\n(3)Home/Core (Single Language)\n(4)Home/Core N\n(5)Professional\n(6)Professional N'))

            if opicao == 1:
                print(system(f'cscript slmgr.vbs /ipk {codico_ativacao[0]}'))
                print(system('cscript slmgr.vbs /skms kms.lotro.cc'))
                print(system('cscript slmgr.vbs /ato'))
            elif opicao == 2:
                print(system(f'cscript slmgr.vbs /ipk {codico_ativacao[1]}'))
                print(system('cscript slmgr.vbs /skms kms.lotro.cc'))
                print(system('cscript slmgr.vbs /ato'))
            elif opicao == 3:
                print(system(f'cscript slmgr.vbs /ipk {codico_ativacao[2]}'))
                print(system('cscript slmgr.vbs /skms kms.lotro.cc'))
                print(system('cscript slmgr.vbs /ato'))
            elif opicao == 4:
                print(system(f'cscript slmgr.vbs /ipk {codico_ativacao[3]}'))
                print(system('cscript slmgr.vbs /skms kms.lotro.cc'))
                print(system('cscript slmgr.vbs /ato'))
            elif opicao == 5:
                print(system(f'cscript slmgr.vbs /ipk {codico_ativacao[4]}'))
                print(system('cscript slmgr.vbs /skms kms.lotro.cc'))
                print(system('cscript slmgr.vbs /ato'))
            elif opicao == 6:
                print(system(f'cscript slmgr.vbs /ipk {codico_ativacao[5]}'))
                print(system('cscript slmgr.vbs /skms kms.lotro.cc'))
                print(system('cscript slmgr.vbs /ato'))
            else:
                print('Escolha uma opição valida!')
    
    elif opicao == 2:
           
           link_url = r'https://github.com/abbodi1406/vcredist/releases/download/v0.73.0/VisualCppRedist_AIO_x86_x64.exe'
           webbrowser.open(link_url)
           sleep(15)
           system('start VisualCppRedist_AIO_x86_x64.exe')
           sleep(2)
           py.press('Enter')
           
           
           