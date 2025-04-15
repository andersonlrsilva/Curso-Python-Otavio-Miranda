
class Foo:
    def __init__(self, multi):
        self.saida = multi

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado*self.saida
        return interna


@Foo(1)
def soma(x, y):
    tot = x+y
    return tot


conta = soma(3, 5)
print(conta)
