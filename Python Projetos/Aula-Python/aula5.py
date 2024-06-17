nome = input('Digite o seu nome: ').lower()
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('O seu nome contém espaço')
    else:
        print('O seu nome não contém espaço')
    print(f'O seu nome tem {len(nome)} letras')
    print(f'A primera letra do seu nome é: {nome[0]}')
    print(f'A utima letra do seu nome é {nome[-1]}')
else:
    print('Voce deixou os espaço em Branco!')