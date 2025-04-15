"""
Evitar criar funçoes que criam tipos mutaveis.


"""


def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Luiz')
adiciona_clientes('joana', cliente1)


cliente2 = adiciona_clientes('Martha')
adiciona_clientes('Pedro', cliente2)


cliente3 = adiciona_clientes('henrique')


print(cliente1)
print(cliente2)
print(cliente3)
