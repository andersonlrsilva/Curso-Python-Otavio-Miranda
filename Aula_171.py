lista_a = [12, 2, 3, 47, 5, 6, 7]
lista_b = [1, 24, 3, 4, 7]


def somalista(l1, l2): # type: ignore
    soma = []
    # intervalo = min(len(l1), len(l2))
    for i in range(min(len(l1), len(l2))):# type: ignore
        soma.append(l1[i] + l2[i]) # type: ignore
    print(soma) # type: ignore


somalista(lista_a, lista_b)
