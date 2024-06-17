try:
    var = input('Digite um numero: ')

    var_floot = float(var)

    numero_impa = var_floot % 2 == 0
    par_mumero_txt = 'ímpa'
    if numero_impa:
        par_mumero_txt = 'par'

    print(f'o numero é {var_floot} é {par_mumero_txt}')

except:
    print('Voce não digitou um numero inteiro! ')