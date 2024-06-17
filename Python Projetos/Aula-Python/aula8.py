try:
    entrada = input('Digite as horas em numero inteiro: ')

    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print(f'bom dia {hora}')
    elif hora >= 12 and hora <= 17:
        print(f'boa tarde {hora}')
    elif hora >= 18 and hora <= 23:
        print(f'Boa noite {hora}')
    else:
        print('Não conheço essa hora!')
except:
    print('Opção Ivalida')