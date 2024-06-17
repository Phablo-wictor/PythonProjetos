nome = input('Seu nome: ')

if len(nome) <= 4:
    print('o seu nome e muito curto!') 

elif len(nome) == 5 or len(nome) == 6:
    print('o seu nome é normal')

elif len(nome) >= 6:
    print('o seu nome é muito grande') 