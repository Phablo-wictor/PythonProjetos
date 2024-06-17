qtd_linha = 5
qtd_coluna = 5

linha = 1

while linha <= qtd_linha:
    conula = 1
    while conula <= qtd_coluna:
        print(f'{linha=} {conula=}')
        conula += 1
    linha += 1
print("acabou")