produtos = {
'nome': 'p1' , 'preco': 10,
'nome': 'p2' , 'preco': 20,
'nome': 'p3' , 'preco': 30,
'nome': 'p4' , 'preco': 40,

}

novos_produtos = [
    {**produtos, 'preco': produtos['preco'] * 1.5 }
    if produtos['preco'] > 20 else {**produtos}
    for produtos in produtos

]


print(novos_produtos)