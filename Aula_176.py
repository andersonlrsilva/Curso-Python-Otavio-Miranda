from functools import partial
from types import GeneratorType


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


def multiplica(preco):
    v = preco * 1.1, 2
    return v


novos_produtos = [{**p, 'preco': multiplica(p['preco'])} for p in produtos]
for itens in novos_produtos:
    print(itens)
