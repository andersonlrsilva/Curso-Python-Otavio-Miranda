from functools import reduce


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# usando função reduce

def funcao_do_reduce(acumulador, produto):
    return acumulador + produto['preco']


total = reduce(funcao_do_reduce, produtos, 0)
print(f'O total é: {total:.2f}')


# usando for
total = 0
for p in produtos:
    total += p['preco']
print(f'{total:.2f}')


print()
print('soma direto no print com list compreesion')
print(sum([p['preco'] for p in produtos]))
