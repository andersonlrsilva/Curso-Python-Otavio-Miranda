lista_a = [12, 2, 3, 47, 5, 6, 7]
lista_b = [1, 24, 3, 4, 7]


def somalista(l1, l2):
    soma = []
    # intervalo = min(len(l1), len(l2))
    for i in range(min(len(l1), len(l2))):
        soma.append(l1[i] + l2[i])
    print(soma)


somalista(lista_a, lista_b)
