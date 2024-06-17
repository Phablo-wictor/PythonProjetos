import requests
import json 
import datetime
import time

for i in range(50):
    
    requi = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')

    dic = json.loads(requi.text)
    moeda0 = dic["USDBRL"]["high"]
    moeda1 = dic["USDBRL"]["pctChange"]

    print('Moeda Brasileira:', "%.2f" %float(moeda0), " Data:", datetime.datetime.now())
    print('Dóla Americano: ', moeda1, " Data:",  datetime.datetime.now())
    print(end='\n')
    time.sleep(5)
