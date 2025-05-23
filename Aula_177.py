

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# novos_produtos = [p for p in produtos if p['preco'] <= 10]


def filtrar_precos(produtos):
    return produtos['preco'] > 100


novo_produtos = filter(filtrar_precos, produtos)


print_iter(novo_produtos)
