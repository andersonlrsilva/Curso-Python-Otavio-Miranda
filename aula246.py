# Classes decoradoras (Decorator classes)

class Multiplicar:
    def __init__(self, mult):
        # self.func = func
        self.mult = mult

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.mult
        return interna


@Multiplicar(10)
def soma(x, y):
    return x + y


var = soma(4, 5)
print(var)
